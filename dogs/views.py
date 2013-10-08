from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from dogs.models import *
from django.contrib.auth.models import User

def index(request):
    users = User.objects
    context = {'users': users}
    return render(request, 'dogs/index.html', context)