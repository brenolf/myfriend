from django.conf.urls import patterns, url

from dogs import dogs_views
from dogs import persons_views

urlpatterns = patterns('',
 url(r'^$', dogs_views.index, name='index'),
 url(r'^persons/create$',
   persons_views.create, name='create-person'),
  url(r'^persons/answer$',
   persons_views.createanswers, name='create-answer'),
 url(r'^persons/edit/$',
   persons_views.create, name='edit-person'),

 url(r'^dogs/create$',
   dogs_views.create, name='create-dog'),
 url(r'^dogs/(?P<dog_id>\d+)/edit/$',
   dogs_views.edit, name='edit-dog'),
 url(r'^dogs/(?P<dog_id>\d+)/remove/$',
   dogs_views.removeDog, name='remove-dog'),
 url(r'^dogs/(?P<dog_id>\d+)/$',
   dogs_views.detail, name='detail-dog'),


  url(r'^testimonials/create$',
   dogs_views.createtestimonial, name='create-testimonial'),
  url(r'^testimonials/$',
   dogs_views.searchTestimonial, name='search-testimonial'),
 url(r'^testimonials/(?P<t_id>\d+)/edit/$',
   dogs_views.edittestimonial, name='edit-testimonial'),
  url(r'^testimonials/(?P<t_id>\d+)/remove/$',
   dogs_views.removetestimonial, name='remove-testimonial'),
 url(r'^testimonials/(?P<t_id>\d+)/$',
   dogs_views.detailtestimonial, name='detail-testimonial'),
  url(r'^dogs/search/$',
   dogs_views.search, name='search-dog'),

 url(r'^persons/(?P<person_username>\d+)/$',
   persons_views.detail, name='detail-person'),
 url(r'^login/$', 'django.contrib.auth.views.login',
   {'template_name': 'auth/signin.html'}),
 url(r'^dogs/search/$',
   dogs_views.search, name='search-dog'),
 url(r'^about/$', dogs_views.about, name='about'),
 url(r'^help/$', dogs_views.help, name='help'),
 url(r'^user/$', dogs_views.user, name='user'),
 url(r'^thread/$', dogs_views.get_thread),
 url(r'^send_message/$', dogs_views.send_message),
 url(r'^dog_images/(?P<filename>.+)$',dogs_views.image_view, name='image_view'),
 )
