from django.conf.urls.defaults import *
from django.contrib import admin, databrowse
admin.autodiscover()

urlpatterns = patterns('',
    (r'^monitor/', include('apps.mon.urls')),
)
