from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from dogs.models import *


@login_required(login_url='/accounts/login/')
def send(request):
	if request.method == 'POST' and 'recipient' in request.POST and
	'content' in request.POST:
		thread = None
		if 'subject' in request.POST:
			thread = MessageThread(subject=request.POST['subject'])
			thread.save()
		else if 'threadid' in request.POST:
			thread = MessageThread.objects.get(pk=request.POST['threadid'])
		else:
			#server error
			return render(request, 'dogs/index.html', {})
		recipient=Person.objects.get(pk=request.POST['recipient'])
		message = Message(thread=thread, sender=request.user,recipient=recipient,
			content=request.POST['recipient'])
		message.save()
	else:
		#server error
		return render(request, 'dogs/index.html', {})

def view(request, thread_id):
	thread = get_object_or_404(MessageThread, pk=thread_id)
	return render(request, 'threads/thread.html', {'thread': thread,})
