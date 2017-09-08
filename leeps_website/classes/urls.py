from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'(?P<class_name>[\w-]+)/(?P<tag_name>.+)', get_readings_by_tag),
    url(r'(?P<class_name>[\w-]+)', details),
]
