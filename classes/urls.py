from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.classes.views',
    (r'^$', 'index'),
    (r'(?P<class_name>[\w-]+)/(?P<tag_name>.+)', 'get_readings_by_tag'),
    (r'(?P<class_name>[\w-]+)', 'details'),
)
