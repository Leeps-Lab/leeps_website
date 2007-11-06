from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    # Example:
    (r'^papers/', include('leeps_website.papers.urls')),
    (r'^people/', include('leeps_website.people.urls')),
    (r'^projects/', include('leeps_website.projects.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.getcwd()+'/site_media/'}),
)

urlpatterns += patterns('leeps_website.views',
    (r'^$|^home/$', 'home'),
    (r'^about/$', 'about'),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^calendar/$', 'direct_to_template', {'template': 'calendar.html'}),
)
