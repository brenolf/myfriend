from django.conf.urls import patterns, url

from dogs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^createperson$', views.createperson, name='createperson'),
    url(r'^(?P<dog_id>\d+)/$', views.detail, name='detail'),
)