from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.papers.views',
    (r'^$', 'index'),
    (r'^by_title/$', 'by_title'),
    (r'^by_date/$', 'by_date'),
)
