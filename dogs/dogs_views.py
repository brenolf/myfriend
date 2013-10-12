from django.shortcuts import render, get_object_or_404

from dogs.models import *


def index(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'dogs/index.html', context)


def detail(request, dog_id):
    dog = get_object_or_404(Dog, pk=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})


def create(request):  # depois mudar pra ficar restful
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form_address = AddressForm(request.POST)
        form_dog = DogForm(request.POST)
        if form_address.is_valid():
            address = form_address.save()
            if form_dog.is_valid():
                dog = form_dog.save(commit=False)
                dog.address = address
                dog.save()
            else:
                return render(request, 'dogs/create.html', {
                    'form_dog': form_dog,
                    'form_address': form_address,
                })
            return HttpResponseRedirect('/dogs')  # Redirect after POST
    else:
        form_dog = DogForm()  # An unbound form
        form_address = AddressForm()

    return render(request, 'dogs/create.html', {
        'form_dog': form_dog,
        'form_address': form_address,
    })
