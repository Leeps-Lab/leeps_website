from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.projects.views',
    (r'^(?P<archived>archived/)?$', 'index'),
    (r'^(?P<archived>archived/)?by_(?P<order>[A-Za-z\-_]+)/$', 'index'),
)
