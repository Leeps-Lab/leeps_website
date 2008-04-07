from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.scriptr.views',
    (r'^$', 'index'),
    (r'^(?P<slug>[\w\-_]+)/$', 'details'),
)
