from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.core import serializers
from django.shortcuts import render_to_response
import json


from dogs.models import *

# python manage.py schemamigration dogs --auto
# python manage.py migrate dogs


@login_required(login_url='/accounts/login/')
def user(request):
	dogs = request.user.person.in_adoption_by.all().order_by('name') | request.user.person.adopted_by.all().order_by('name')

	context = {'user': request.user, 'dogs': dogs}
	if request.method == 'POST' and 'remove' in request.POST:
		dogid = request.POST['remove']
		d = Dog.objects.get(pk=dogid)
		d.delete()

	return render(request, 'persons/user.html', context)


def about(request):
	return render(request, 'general/about.html', {})


def index(request):
	dogs = Dog.objects.all()[:10]
	context = {'dogs': dogs}
	return render(request, 'dogs/index.html', context)


def detail(request, dog_id):
	dog = get_object_or_404(Dog, pk=dog_id)

	if request.method == 'POST' and request.user.is_authenticated() and not dog.in_adoption_process and not dog.adopted:

		message_form = MessageForm(request.POST)

		if message_form.is_valid():
			thread = MessageThread(subject = 'subject', person1 = request.user.person, person2 = dog.in_adoption_by, related_dog = dog)
			thread.save()

			message = message_form.save(commit = False)
			message.thread = thread
			message.sender = request.user.person
			message.save()

			dog.adopted_by = request.user.person
			dog.in_adoption_process = True
			dog.adopted = False
			dog.save()
		else:
			print '----------------- Erro tentando adotar cachorro!'

	color = dict(Dog.COLOR_CHOICES)[dog.color]
	size = dict(Dog.SIZE_CHOICES)[dog.size]
	letter = 'o' if dog.gender == 'M' else 'a'
	
	available = (not dog.adopted and not dog.in_adoption_process) and (request.user.is_authenticated() and dog.in_adoption_by.user.id != request.user.id) 

	return render(request, 'dogs/dog.html', {'dog': dog, 'user': request.user, 'color': color, 'size': size, 'genderLetter': letter, 'dogIsAvailable': available})


def search(request):
	if 'breed' not in request.GET or 'size' not in request.GET or 'color' not in request.GET or request.GET['breed'] == '' or request.GET['size'] == '' or request.GET['color'] == '':
		return render(request, 'dogs/search.html', {'breeds': Breed.objects.all()})

	else:
		dogs = Dog.objects.all().filter(adopted = False, in_adoption_process = False)
		
		if request.user.is_authenticated():
			dogs = dogs.exclude(in_adoption_by = request.user.person)

		if request.GET['color'] == 'Todas':
			color = 'Todas'
		else:
			color = dict(Dog.COLOR_CHOICES)[request.GET['color']]
			dogs = dogs.filter(color=request.GET['color'])
		if request.GET['size'] == 'Todas':
			size = 'Todas'
		else:
			size = dict(Dog.SIZE_CHOICES)[request.GET['size']]
			dogs = dogs.filter(size=request.GET['size'])
		if request.GET['breed'] != 'Todas':
			dogs = dogs.filter(breed__breed_name=request.GET['breed'])

		context = {
			'color': color,
			'size': size,
			'breed': request.GET['breed'],
			'dogs': dogs
		}

		return render(request, 'dogs/list-dogs.html', context)


@login_required(login_url='/accounts/login/')
def create(request):  # depois mudar pra ficar restful
	if request.method == 'POST':  # If the form has been submitted...
		# A form bound to the POST data
		form_dog = DogForm(request.POST, request.FILES)
		if form_dog.is_valid():
			dog = form_dog.save(commit=False)
			x = request.user
			dog.in_adoption_by = request.user.person
			dog.save()
		else:
			return render(request, 'dogs/newdog.html', {
				'form_dog': form_dog,
				'error': True
			})
		return HttpResponseRedirect('/')  # Redirect after POST
	else:
		form_dog = DogForm()  # An unbound form

	return render(request, 'dogs/newdog.html', {
		'form_dog': form_dog,
	})


@login_required(login_url='/accounts/login/')
def edit(request, dog_id):  # depois mudar pra ficar restful
	dog = get_object_or_404(Dog, pk=dog_id)
	if dog.in_adoption_by != request.user.person:
		return render(request, 'index.html', {})
	if request.method == 'POST':  # If the form has been submitted...
		# A form bound to the POST data
		form_dog = DogForm(request.POST, request.FILES)
		if form_dog.is_valid():
			dog = form_dog.save(commit=False)
			dog.id = dog_id
			x = request.user
			dog.in_adoption_by = request.user.person
			dog.save()
		else:
			return render(request, 'dogs/newdog.html', {
				'form_dog': form_dog,
				'error': True
			})
		return HttpResponseRedirect('/')  # Redirect after POST
	else:
		# An unbound form
		form_dog = DogForm(instance=get_object_or_404(Dog, pk=dog_id))

	return render(request, 'dogs/newdog.html', {
		'form_dog': form_dog,
	})


def get_thread(request):
	if not request.user.is_authenticated():
		return HttpResponse('This thread is blocked for you', mimetype='text/plain')

	dog = Dog.objects.get(pk = int(request.POST['dog']))

	if dog.adopted_by.user.id == request.user.id:
		thread = MessageThread.objects.all().filter(related_dog = dog, person1 = request.user.person)

		if not thread:
			raise Exception('Thread inexistente')
		else:
			thread = thread.latest('date')
	else:
		thread = MessageThread.objects.all().filter(related_dog = dog, person2 = request.user.person)

		if not thread:
			raise Exception('Thread inexistente')
		else:
			thread = thread.latest('date')

	msg = Message.objects.all().filter(thread = thread)

	lista = []

	for m in msg:
		nome = m.sender.user.username

		if m.sender.user.id == request.user.id:
			nome = None

		lista.append({
			'content': m.content,
			'user': nome,
			'date': m.date.strftime('%d/%m/%Y')
		})

	return HttpResponse(json.dumps(lista), mimetype='text/javascript; charset=utf-8')

def send_message(request):
	if not request.user.is_authenticated():
		return HttpResponse('This thread is blocked for you', mimetype='text/plain')

	response = True

	def getBool(str):
		if str == 'False' or str == 'false' or str == '0':
			return False			
		return True

	deny = getBool(request.POST['deny'])
	allow = getBool(request.POST['allow'])
	dog = Dog.objects.get(pk = int(request.POST['dog']))

	if not deny and not allow:

		if dog.adopted_by.user.id == request.user.id:
			thread = MessageThread.objects.all().filter(related_dog = dog, person1 = request.user.person)

			if not thread:
				response = False
			else:
				thread = thread.latest('date')
		else:
			thread = MessageThread.objects.all().filter(related_dog = dog, person2 = request.user.person)

			if not thread:
				response = False
			else:
				thread = thread.latest('date')

		if response:
			message = Message(thread = thread, sender = request.user.person, content = request.POST['content'])
			message.save()

	elif request.user.id == dog.in_adoption_by.user.id:

		if deny:
			# dog.adopted_by = None
			dog.adopted = False
			dog.in_adoption_process = False
			dog.save()

		elif allow:
			dog.adopted = True
			dog.in_adoption_process = False
			dog.save()

	return HttpResponse(json.dumps({'ok': response}), mimetype='text/javascript; charset=utf-8')