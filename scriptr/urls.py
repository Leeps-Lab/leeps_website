from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.scriptr.views',
    (r'^$', 'index'),
    (r'^(?P<scriptslug>\w+)/$', 'run_script'),
)
