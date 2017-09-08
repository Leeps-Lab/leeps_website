from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<archived>archived/)?$', index),
    url(r'^(?P<archived>archived/)?by_(?P<order>[A-Za-z\-_]+)/$', index),
    url(r'^$', index),
]
