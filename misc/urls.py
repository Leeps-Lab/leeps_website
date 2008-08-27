from django.conf.urls.defaults import *

urlpatterns = patterns('leeps_website.misc.views',
    (r'^$', 'index'),
    (r'^page/(?P<slug>.*)/$', 'page'),
    (r'^category/(?P<slug>.*)/$', 'category'),
)
