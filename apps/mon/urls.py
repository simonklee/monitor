from django.conf.urls.defaults import *

urlpatterns = patterns('apps.mon.views',
    url(r'^(?P<pattern>.+)?$',
        'mon_mon',
        name = 'mon_mon'),

)
