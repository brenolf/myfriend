from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from dogs.models import *


def index(request):
    dogs = Dog.objects.all()[:10]
    context = {'dogs': dogs}
    return render(request, 'dogs/index.html', context)


def detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dogs/dog.html', {'dog': dog})
    
def search(request):
	if 'breed' not in request.GET or 'size' not in request.GET or 'color' not in request.GET:
		return render(request, 'dogs/search.html', {'breeds': Breed.objects.all()})
	else:
		dogs=Dog.objects.filter(breed__breed_name=request.GET['breed'],
	size=request.GET['size'], color=request.GET['color'])
		context = {
		'color':dict(Dog.COLOR_CHOICES)[request.GET['color']],
		'size':dict(Dog.SIZE_CHOICES)[request.GET['size']],
		'breed':request.GET['breed'],
		'dogs':dogs
		}
		return render(request, 'dogs/list-dogs.html', context)

@login_required(login_url='/accounts/login/')
def create(request):  # depois mudar pra ficar restful
	if request.method == 'POST':  # If the form has been submitted...
		# A form bound to the POST data
		form_dog = DogForm(request.POST, request.FILES)
		if form_dog.is_valid():
			dog = form_dog.save(commit=False)
			x=request.user
			dog.in_adoption_by = request.user.person
			dog.save()			
		else:
			return render(request, 'dogs/newdog.html', {
				'form_dog': form_dog,
				'error':True
			})
		return HttpResponseRedirect('/dogs')  # Redirect after POST
	else:
		form_dog = DogForm()  # An unbound form

	return render(request, 'dogs/newdog.html', {
		'form_dog': form_dog,
	})
