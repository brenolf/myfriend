from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from dogs.models import *
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def create(request):  # depois mudar pra ficar restful
    user=request.user
    if request.method == 'POST':  # If the form has been submitted...
        # A form bound to the POST data

        form_address = AddressForm(request.POST)
        form_person = PersonForm(request.POST)
        form_user = UserForm(request.POST)
        
        if form_address.is_valid() and form_user.is_valid():
            user.first_name = form_user.cleaned_data['first_name']
            user.last_name = form_user.cleaned_data['last_name']
            address = form_address.save()
            if form_person.is_valid():
                person = form_person.save(commit=False)
                person.address = address
                person.id = user.person.id
                user.person = person
                person.save()
                user.save()
                return HttpResponseRedirect('/')

            else:
                return render(request, 'persons/create.html', {
                    'form_person': form_person,
                    'form_address': form_address,
                    'form_user': form_user,
                    'user': request.user,
                })
        else:
            return render(request, 'persons/create.html', {
                    'form_person': form_person,
                    'form_address': form_address,
                    'form_user': form_user,
                    'user': request.user,
                })
            return HttpResponseRedirect('/')  # Redirect after POST
    else:
        form_person = PersonForm(instance=request.user.person)
        form_address = AddressForm(instance=request.user.person.address)
        form_user = UserForm(instance=request.user)

    print request.user.first_name


    return render(request, 'persons/create.html', {
        'form_person': form_person,
        'form_address': form_address,
        'form_user': form_user,
        'user': request.user,
    })


def detail(request, person_username):
    user = get_object_or_404(User, pk=person_username)
    person = user.person
    return render(request, 'persons/detail.html', {'person': person})
