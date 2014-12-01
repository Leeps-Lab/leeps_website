from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.people.views',
    (r'details/(?P<person>[\w-]+)', 'details'),
    (r'(?P<category>[\w-]+)', 'category'),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'redirect_to', {'url' : '/people/faculty'}),
)

