from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^m/', include('apps.mon.urls')),
    url(r'^$', direct_to_template, {'template': 'mon/mon_api.html'}, name='index'),
)
