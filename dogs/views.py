from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from dogs.models import *
from django.contrib.auth.models import User


def index(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'dogs/index.html', context)

def detail(request, dog_id):
    dog = get_object_or_404(Poll, pk=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})

def createperson(request): #depois mudar pra ficar restful
	if request.method == 'POST': # If the form has been submitted...
		form = PersonForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
			return HttpResponseRedirect('dogs/index.html') # Redirect after POST
	else:
		form = PersonForm() # An unbound form

	return render(request, 'dogs/createperson.html', {
		'form': form,
	})