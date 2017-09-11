from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import RedirectView
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^papers/', include('leeps_website.papers.urls')),
    url(r'^classes/', include('leeps_website.classes.urls')),
    url(r'^misc/', include('leeps_website.misc.urls')),
    url(r'^projects/', include('leeps_website.projects.urls')),
    url(r'^people/', include('leeps_website.people.urls')),

    url(r'^calendar/$', RedirectView.as_view(url='http://econlab.ucsc.edu/public/show_calendar.php'))

    url(r'^$', RedirectView.as_view(url='/home'))
    
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
