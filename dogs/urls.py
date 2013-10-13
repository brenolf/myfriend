from django.conf.urls import patterns, url

from dogs import dogs_views
from dogs import persons_views

urlpatterns = patterns('',
                       url(r'^$', dogs_views.index, name='index'),
                       url(r'^persons/create$',
                           persons_views.create, name='create'),
                       url(r'^dogs/create$', dogs_views.create, name='create'),
                       url(r'^dogs/(?P<dog_id>\d+)/$',
                           dogs_views.detail, name='detail'),
                       url(r'^persons/(?P<person_username>\w+)/$',
                           persons_views.detail, name='detail'),
                       url(r'^login/$', 'django.contrib.auth.views.login', {
                       'template_name': 'auth/signin.html'}),
                       )
