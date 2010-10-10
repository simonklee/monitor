from django.conf.urls.defaults import *
from django.contrib import admin, databrowse
admin.autodiscover()

urlpatterns = patterns('',
    (r'^m/', include('apps.mon.urls')),
)
