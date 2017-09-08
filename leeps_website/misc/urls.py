from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^page/(?P<slug>.*)/$', page),
    url(r'^category/(?P<slug>.*)/$', category),
]
