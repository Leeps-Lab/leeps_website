from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.papers.views',
    (r'^$', 'index'),
    (r'^sort-by-date/(?P<order>\w+)/$', 'sort_by_date'),
    (r'^filter-by-keyword$', 'filter_by_keyword'),
    (r'^filter-by-author$', 'filter_by_author'),
)

