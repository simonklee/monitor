from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('apps.chart.views',

    url(r'^m/(?P<pattern>.+)?$', 'chart_generator',
        {'template_name': 'chart/chart_generator.html'},
        name = 'chart_generator'),

    url(r'^$', direct_to_template,
        {'template': 'chart/chart_chart.html'},
        name='chart'),
)
