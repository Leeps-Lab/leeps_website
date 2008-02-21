from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    # app content
    (r'^papers/', include('leeps_website.papers.urls')),
    (r'^people/', include('leeps_website.people.urls')),
    (r'^projects/', include('leeps_website.projects.urls')),
    (r'^classes/', include('leeps_website.classes.urls')),

    # admin
    (r'^admin/', include('django.contrib.admin.urls')),
    
    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.getcwd()+'/site_media/'}),
)

urlpatterns += patterns('leeps_website.views',
    # main content
    (r'^$|^home/$', 'home'),
    (r'^about/$', 'about'),
)

urlpatterns += patterns('django.views.generic.simple',
    # simple redirect
    (r'^calendar/$', 'redirect_to', {'url': 'http://econlab.ucsc.edu/public/show_calendar.php'}),
)
