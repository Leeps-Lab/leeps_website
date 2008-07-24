from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.fire.views',
    (r'^new_session/$', 'new_session'),
)
