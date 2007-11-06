from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.projects.views',
    (r'^$', 'index'),
    (r'^by_name/$', 'by_name'),
    (r'^by_date/$', 'by_date'),
    (r'^by_grant/$', 'by_grant'),
)
