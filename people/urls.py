from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.people.views',
    (r'^$', 'index'),
    (r'(?P<person>[\w-]+)', 'details'),
)
