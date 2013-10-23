from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from dogs.models import *


@login_required(login_url='/accounts/login/')
def user(request):
    dogs = request.user.person.in_adoption_by.all()
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
    if request.method == 'POST' and request.user:
        dog.adopted_by = request.user.person
        dog.adopted = True
        dog.save()
    color = dict(Dog.COLOR_CHOICES)[dog.color]
    size = dict(Dog.SIZE_CHOICES)[dog.size]
    return render(request, 'dogs/dog.html', {'dog': dog, 'user': request.user, 'color': color, 'size': size})


def search(request):
    if 'breed' not in request.GET or 'size' not in request.GET or 'color' not in request.GET or request.GET['breed'] == '' or request.GET['size'] == '' or request.GET['color'] == '':
        return render(request, 'dogs/search.html', {'breeds': Breed.objects.all()})

    else:
        dogs = Dog.objects.all().filter(adopted = False)
        
        if request.user:
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
