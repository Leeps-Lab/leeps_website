from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.fire.views',
    (r'^new_session/((?P<kindling>[^/])/(?P<configuration>[^/])/)?$', 'new_session'),
    (r'^sessions/$', 'sessions'),
    (r'^experiments/$', 'experiments'),
)
