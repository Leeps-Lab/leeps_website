from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^sort-by-date/(?P<order>\w+)/$', sort_by_date),
    url(r'^filter-by-keyword$', filter_by_keyword),
    url(r'^filter-by-author$', filter_by_author),
]
