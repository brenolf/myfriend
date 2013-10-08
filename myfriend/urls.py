from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myfriend.views.home', name='home'),
    # url(r'^myfriend/', include('myfriend.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	url(r'^teste/', include('teste.urls')),
	url(r'^dogs/', include('dogs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
