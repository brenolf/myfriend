#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import *
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
from django.core import serializers
from django.shortcuts import render_to_response
import json
from django.contrib import messages
from django.core.mail import send_mail
import os
from django.conf import settings
from django.utils._os import safe_join
from database_storage import DatabaseStorage
from django.core.exceptions import ObjectDoesNotExist
import mimetypes

from dogs.models import *
from allauth.account.models import *

# python manage.py schemamigration dogs --auto
# python manage.py migrate dogs


def image_view(request, filename):
     # Read file from database
    storage = DatabaseStorage(DBS_OPTIONS)
    image_file = storage.open(filename, 'rb')
    if not image_file:
        raise Http404
    file_content = image_file.read()
   
    # Prepare response
    content_type, content_encoding = mimetypes.guess_type(filename)
    response = HttpResponse(content=file_content, mimetype=content_type)
    response['Content-Disposition'] = 'inline; filename=%s' % filename
    if content_encoding:
        response['Content-Encoding'] = content_encoding
    return response


@login_required(login_url='/accounts/login/')
def user(request):
	dogs = request.user.person.in_adoption_by.all().order_by('name') | request.user.person.adopted_by.all().order_by('name')
	testimonials = request.user.person.adopter.all()

	context = {'user': request.user, 'dogs': dogs, 'testimonials': testimonials}

	if request.method == 'POST' and 'removet' in request.POST:
		tid = request.POST['removet']
		d = Testimonial.objects.get(pk=tid)
		d.delete()

	if request.method == 'POST' and 'abadocao' in request.POST:
		dogid = request.POST['abadocao']
		d = Dog.objects.get(pk=dogid)
		d.in_adoption_by = request.user.person
		d.in_adoption_process = False
		d.abandoned = False
		d.adopted = False
		d.adopted_by = None
		d.save()

	return render(request, 'persons/user.html', context)


def about(request):
	return render(request, 'general/about.html', {})


def index(request):
	# racas = ["Akita Inu", "Beagle", "Beagle Harrier", "Bobtail", "Boiadeiro de Berna", "Boxer", "Braco Alemão", "Braco Francês", "Bull Terrier Inglês", "Bulldog Americano", "Bulldog Inglês", "Cairn Terrier", "Cane Corso", "Caniche", "Cão de Crista Chinês", "Cão d’Água Espanhol", "Cão Lobo Checoslovaco", "Cavalier King Charles Spaniel", "Chihuahua", "Chow-Chow", "Cocker Americano", "Cocker Spaniel Inglês", "Collie", "Dálmata", "Doberman", "Dogue Alemão", "Dogue de Bordéus", "Epagneul Bretão", "Fila Brasileiro", "Fox Terrier", "Galgo Afegão", "Golden Retriever", "Husky Siberiano", "Ibizan Hound", "Jack Russel Terrier", "Lhasa Apso", "Mastiff", "Mastim dos Pirenéus", "Mastim Espanhol", "Mastim Napolitano", "Norfolk Terrier", "Papillon", "Pastor Alemão", "Pastor de Beauce", "Pequeno Basset Griffon", "Pequeno Brabançon", "Pequeno Cão Leão", "Pequinês", "Perdigueiro Português", "Pinscher Anão", "Pitbull", "Rottweiler", "Samoiedo", "São Bernardo", "Schnauzer", "Setter Inglês", "Setter Irlandês", "Shar Pei", "Shih Tzu", "Spaniel Japonês", "Spitz Alemão", "Staffordshire Bull Terrier", "Teckel", "Terranova", "Terrier Brasileiro", "Vizsla", "Waimaraner", "West Highland White Terrier", "Yorkshire Terrier"]

	dogs = Dog.objects.all()[:10]
	context = {'dogs': dogs}
	return render(request, 'dogs/index.html', context)

def detailtestimonial(request, t_id):
	t = get_object_or_404(Testimonial, pk=t_id)
	return render(request, 'dogs/testimonial.html', {'t':t})



def detail(request, dog_id):
	dog = get_object_or_404(Dog, pk=dog_id)
	c = dog.characteristics

	if request.method == 'POST' and request.user.is_authenticated() and not dog.in_adoption_process and not dog.adopted:

		message_form = MessageForm(request.POST)

		if message_form.is_valid():
			thread = MessageThread(subject = 'subject', person1 = request.user.person, person2 = dog.in_adoption_by, related_dog = dog)
			thread.save()

			message = message_form.save(commit = False)
			message.thread = thread
			message.sender = request.user.person
			message.closed = False
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
	if c != None:
		c = CharacteristicsForm(data=model_to_dict(c))
	jaccard = False
	if request.user.is_authenticated():
		jaccard = similarity_dog(request, dog)
		if jaccard != -1:
			jaccard=jaccard*100;
			jaccard=int(jaccard)


	charsList = dog.characteristics.__dict__
	hasChars = False
	
	for c in charsList:
		hasChars = c[0] != '_' and c != 'id' and charsList[c] != None

	return render(request, 'dogs/dog.html', {'dog': dog,
	 'user': request.user, 
	 'color': color,
	 'size': size,
	 'genderLetter': letter, 
	 'dogIsAvailable': available, 
	 'char': c,
	 'hasChars': hasChars,
	 'jaccard': jaccard})


def searchTestimonial(request):
	x=Testimonial.objects.all()
	context={'testimonials':x}
	return render(request, 'dogs/list-testimonials.html', context)


def search(request):
	messages.info(request, 'Three credits remain in your account.')
	if 'breed' not in request.GET or 'size' not in request.GET or 'color' not in request.GET or request.GET['breed'] == '' or request.GET['size'] == '' or request.GET['color'] == '':
		r = Breed.objects.all()
		rn = len(r)
		return render(request, 'dogs/search.html', {'breeds': r, 'results': rn})

	elif 'personalidade' in request.GET:
		if not request.user.is_authenticated():
			return HttpResponseRedirect('/accounts/login/')
		color = 'Todas'
		size = 'Todas'
		breed = 'Todas'
		dogs, indexes = similar_dogs(request)

		rn = len(dogs)

		context = {
			'color': color,
			'size': size,
			'breed': request.GET['breed'],
			'dogs': dogs,
			'indexes': indexes,
			'results': rn,
		}

		return render(request, 'dogs/list-dogs.html', context)
		
	else:
		dogs = Dog.objects.all().filter(adopted = False, in_adoption_process = False)
		if 'abandonado' in request.GET:
			dogs=dogs.filter(abandoned = True)
		else:
			dogs=dogs.filter(abandoned = False)
		
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

		rn = len(dogs)

		context = {
			'color': color,
			'size': size,
			'breed': request.GET['breed'],
			'dogs': dogs,
			'indexes': False,
			'results': rn
		}

		return render(request, 'dogs/list-dogs.html', context)

		




#form.rate.queryset = Rate.objects.filter(company_id=the_company.id)
@login_required(login_url='/accounts/login/')
def createtestimonial(request):  # depois mudar pra ficar restful
	if request.method == 'POST':  # If the form has been submitted...
		# A form bound to the POST data
		form_testimonial = TestimonialForm(request.POST, request.FILES)
		if form_testimonial.is_valid():
			t = form_testimonial.save(commit=False)
			t.adopter = t.dog.adopted_by
			t.giver = t.dog.in_adoption_by
			t.save()
			return HttpResponseRedirect('/testimonials/'+str(t.id)+"/") 
		else:
			return render(request, 'dogs/newtestimonial.html', {
				'form_testimonial': form_testimonial,
				'error': True
			})
		return HttpResponseRedirect('/testimonials')  # Redirect after POST
	else:
		form_testimonial = TestimonialForm()
		form_testimonial.fields['dog'].queryset = Dog.objects.filter(adopted_by=request.user.person)

	return render(request, 'dogs/newtestimonial.html', {
		'form_testimonial': form_testimonial,
	})

@login_required(login_url='/accounts/login/')
def create(request):  # depois mudar pra ficar restful
	print 'criar'
	if request.method == 'POST':  # If the form has been submitted...
		# A form bound to the POST data
		form_dog = DogForm(request.POST, request.FILES)
		form_characteristics = CharacteristicsForm(request.POST, request.FILES)
		c=None
		if form_characteristics.is_valid():
			c = form_characteristics.save()
		else:
			print "erro1"
			return render(request, 'dogs/newdog.html', {
				'form_dog': form_dog,
				'form_characteristics': form_characteristics,
				'error': True
			})
		if form_dog.is_valid():
			dog = form_dog.save(commit=False)
			x = request.user
			dog.in_adoption_by = request.user.person
			dog.characteristics = c
			dog.characteristics.save()
			dog.save()
			print 'salvo! id '+str(dog.id)
			sendemails(request,dog)
			return HttpResponseRedirect('/dogs/'+str(dog.id)+"/") 
		else:
			print "erro2"
			return render(request, 'dogs/newdog.html', {
				'form_dog': form_dog,
				'form_characteristics': form_characteristics,
				'error': True
			})
		return HttpResponseRedirect('/dogs/search')  # Redirect after POST
	else:
		form_dog = DogForm()  # An unbound form
		form_characteristics = CharacteristicsForm()

	return render(request, 'dogs/newdog.html', {
		'form_dog': form_dog,
		'form_characteristics': form_characteristics,
	})

@login_required(login_url='/accounts/login/')
def edittestimonial(request, t_id):
	t = get_object_or_404(Testimonial, pk=t_id)
	if request.method == 'POST':  # If the form has been submitted...
		# A form bound to the POST data
		form_testimonial = TestimonialForm(request.POST, request.FILES)
		if form_dog.is_valid():
			t = form_testimonial.save(commit=False)
			t.adopter = t.dog.adopted_by
			t.giver = t.dog.in_adoption_by
			t.save()
			return HttpResponseRedirect('/testimonials/'+str(t.id)+"/") 
		else:
			return render(request, 'dogs/newtestimonial.html', {
				'form_testimonial': form_testimonial,
				'error': True
			})
		return HttpResponseRedirect('/testimonials')  # Redirect after POST
	else:
		form_testimonial = TestimonialForm(instance=t)
		form_testimonial.fields['dog'].queryset = Dog.objects.filter(adopted_by=request.user.person)

	return render(request, 'dogs/newtestimonial.html', {
		'form_testimonial': form_testimonial,
	})


@login_required(login_url='/accounts/login/')
def removeDog(request, dog_id):
	print 'remover cao'
	dog = get_object_or_404(Dog, pk=dog_id)

	if dog.in_adoption_by != request.user.person:
		return render(request, 'index.html', {})

	if request.method == 'POST':
		dog.delete()
		return HttpResponseRedirect('/user/')

	letter = 'o' if dog.gender == 'M' else 'a'
	
	return render(request, 'dogs/deletedog.html', {'dog': dog, 'genderLetter': letter})

#pegar caracteristicas do dog_id tambem
@login_required(login_url='/accounts/login/')
def edit(request, dog_id):  # depois mudar pra ficar restful
	print 'editar'
	dog = get_object_or_404(Dog, pk=dog_id)
	c = dog.characteristics
	if dog.in_adoption_by != request.user.person:
			return render(request, 'index.html', {})
	
	if request.method == 'POST':	
		form_dog = DogForm(request.POST, request.FILES)
		form_characteristics = CharacteristicsForm(request.POST, request.FILES)	
		if form_characteristics.is_valid():
			c = form_characteristics.save()
		else:
			print "erro1"
			return render(request, 'dogs/newdog.html', {
				'form_dog': form_dog,
				'form_characteristics': form_characteristics,
				'error': True
			})
		if request.method == 'POST':  # If the form has been submitted...
			# A form bound to the POST data
			form_dog = DogForm(request.POST, request.FILES)
			if form_dog.is_valid():
				dog = form_dog.save(commit=False)
				dog.id = dog_id
				dog.characteristics = c
				dog.characteristics.save()
				dog.in_adoption_by = request.user.person
				dog.save()
			else:
				return render(request, 'dogs/newdog.html', {
					'form_dog': form_dog,
					'form_characteristics': form_characteristics,
					'error': True
				})
			return HttpResponseRedirect('/dogs/'+str(dog.id)+"/") 
	else:
		# An unbound form
		dog = get_object_or_404(Dog, pk=dog_id)
		form_dog = DogForm(instance=dog)
		form_characteristics = CharacteristicsForm(instance=c)
		print 'aqui get'
	return render(request, 'dogs/newdog.html', {
		'form_dog': form_dog,
		'form_characteristics': form_characteristics,
		'error': False,
	})



def get_thread(request):
	if not request.user.is_authenticated():
		return HttpResponse('This thread is blocked for you', mimetype='text/plain')

	dog = Dog.objects.get(pk = int(request.POST['dog']))

	if dog.adopted_by.user.id == request.user.id:
		thread = MessageThread.objects.all().filter(related_dog = dog, person1 = request.user.person, closed = False)

		if not thread:
			raise Exception('Thread error')
		else:
			thread = thread.latest('date')
	else:
		thread = MessageThread.objects.all().filter(related_dog = dog, person2 = request.user.person, closed = False)

		if not thread:
			raise Exception('Thread error')
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

	if dog.adopted_by.user.id == request.user.id:
		thread = MessageThread.objects.all().filter(related_dog = dog, person1 = request.user.person, closed = False)

		if not thread:
			response = False
		else:
			thread = thread.latest('date')
	else:
		thread = MessageThread.objects.all().filter(related_dog = dog, person2 = request.user.person, closed = False)

		if not thread:
			response = False
		else:
			thread = thread.latest('date')

	if not deny and not allow and response:
			message = Message(thread = thread, sender = request.user.person, content = request.POST['content'])
			message.save()

	elif request.user.id == dog.in_adoption_by.user.id:
		if deny or allow:
			thread.closed = True
			thread.save()

		if deny:
			dog.adopted_by = None
			dog.adopted = False
			dog.in_adoption_process = False
			dog.save()

		elif allow:
			dog.adopted = True
			dog.in_adoption_process = False
			dog.save()

	return HttpResponse(json.dumps({'ok': response}), mimetype='text/javascript; charset=utf-8')

def similarity_dog(request, dog):
	return similarity_doguser(request.user, dog)

def similarity_doguser(user, dog):
	answer = user.person.answers
	return modified_jaccard(answer,dog.characteristics,dog.size)


def similar_dogs(request):
	answer = request.user.person.answers
	dogs = Dog.objects.all().filter(adopted = False, in_adoption_process = False)
	dogs = dogs.exclude(in_adoption_by = request.user.person)
	dogs = [(modified_jaccard(answer,dog.characteristics,dog.size),dog) for dog in dogs]
	dogs.sort(key=lambda tup: tup[0], reverse=True) 
	dogs2 = [dog[1] for dog in dogs]
	#dogs2 = dogs
	indexes = [dog[0] for dog in dogs]

	return dogs2[:10], indexes



def compare_jaccard(v1, v2, total, equal):
	if v1 is None:
		return total, equal
	if v2 is None:
		return total+0.5, equal
	if v1==v2:
		return total+1, equal+1
	if v1!=v2:
		return total+1, equal

def modified_jaccard(a, c, size): #answer and characteristics
	if a == None or c == None:
		print 'no jaccard for you :(!'
		return -1
	print 'jaccard!'
	total = 0
	equal = 0
	total, equal = compare_jaccard(a.apartment, c.likeinside, total, equal)
	total, equal = compare_jaccard(a.backyard, c.likeoutside, total, equal)
	total, equal = compare_jaccard(a.insidehouse, c.likeinside, total, equal)
	if size=='xs' or size=='s':
		size=True
	else:
		size=False
	total, equal = compare_jaccard(a.smalldogs, size, total, equal)
	total, equal = compare_jaccard(not a.manyguests, c.jealousperson, total, equal)
	#total, equal = compare_jaccard(a.priorexperience, , total, equal)
	total, equal = compare_jaccard(a.time, c.needexercise, total, equal)
	total, equal = compare_jaccard(a.training, c.stubborn, total, equal)
	total, equal = compare_jaccard(a.physicallyactive, c.needexercise, total, equal)
	total, equal = compare_jaccard(a.calmness, c.calm, total, equal)
	total, equal = compare_jaccard(a.likebarks, c.barker, total, equal)
	total, equal = compare_jaccard(a.likeaggressiveness, c.aggressive, total, equal)
	total, equal = compare_jaccard(a.likewalking, c.needexercise, total, equal)
	total, equal = compare_jaccard(a.havemoney, c.expensive, total, equal)
	total, equal = compare_jaccard(a.havemoney, c.medicalcare, total, equal)
	total, equal = compare_jaccard(a.allergy, c.longhair, total, equal)
	total, equal = compare_jaccard(a.allergy, c.hairfall, total, equal)
	total, equal = compare_jaccard(not a.smallanimals, c.hunter, total, equal)
	total, equal = compare_jaccard(not a.otheranimals, c.jealousanimal, total, equal)
	total, equal = compare_jaccard(a.kids, c.likekids, total, equal)
	print "total: ",total, " equal: ",equal
	return equal/float(total)


def sendemails(request, dog):
	print 'entrou send'
	users = User.objects.all()
	emails=[]
	for u in users:
		try:
			if u.person.emaildog != None:
				s=similarity_doguser(u,dog)*100
				print s,' x ',u.person.emaildog
				if s>=int(u.person.emaildog):
					print 'aqui2'
					e=EmailAddress.objects.get(user=u)
					if e.verified:
						emails.append(e.email)
						print 'vai mandar email'
		except:
			print 'except'
					
	send_mail('Novo cão similar a você!', 'Olá! Temos um cão similar a você em ' + request.build_absolute_uri('/dogs/'+str(dog.id)+'/'),
		'myfriend.teste@gmail.com',	emails, fail_silently=True)
