from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from dogs.models import *
from django.contrib.auth.models import User


def create(request):  # depois mudar pra ficar restful
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data
        form_address = AddressForm(request.POST)
        form_person = PersonForm(request.POST)
        if form_address.is_valid():
            address = form_address.save()
            if form_person.is_valid():
                person = form_person.save(commit=False)
                person.address = address
                person.save()
            else:
                return render(request, 'persons/create.html', {
                    'form_person': form_person,
                    'form_address': form_address,
                })
            return HttpResponseRedirect('/dogs')  # Redirect after POST
    else:
        form_person = PersonForm()  # An unbound form
        form_address = AddressForm()

    return render(request, 'persons/create.html', {
        'form_person': form_person,
        'form_address': form_address,
    })


def detail(request, person_username):
    user = get_object_or_404(User, username=person_username)
    person = user.person
    return render(request, 'persons/detail.html', {'person': person})
