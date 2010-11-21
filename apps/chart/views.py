from django.template import RequestContext
from django.shortcuts import render_to_response as render

def chart_generator(request, pattern, template_name, *args, **kwargs):
    if pattern:
        items = pattern.split('/')
        words = ', '.join((f.lower() for f in items if f.isalpha()))
        title = 'filter(%s)' % words
    else:
        title = 'all data'
        pattern = ''

    return render(template_name, {
        'pattern': pattern,
        'title': title,
        'realtime': True if 'realtime' in pattern.lower() else False,
        },
        context_instance=RequestContext(request)
    )
