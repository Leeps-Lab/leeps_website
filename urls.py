from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib import admin

from leeps_website.papers.models import Paper
from leeps_website.people.models import Person
from leeps_website.projects.models import Project
from leeps_website.classes.models import Class
from django.contrib.flatpages.models import FlatPage

admin.autodiscover()

sitemaps = {
    'papers': GenericSitemap({'queryset': Paper.objects.all()}),
    'people': GenericSitemap({'queryset': Person.objects.all()}),
    'projects': GenericSitemap({'queryset': Project.objects.all()}),
    'classes': GenericSitemap({'queryset': Class.objects.all()}),
    'flatpages': GenericSitemap({'queryset': FlatPage.objects.all()}),
}

urlpatterns = patterns('',
    # app content
    (r'^papers/', include('leeps_website.papers.urls')),
    (r'^people/', include('leeps_website.people.urls')),
    (r'^projects/', include('leeps_website.projects.urls')),
    (r'^classes/', include('leeps_website.classes.urls')),
    (r'^misc/', include('leeps_website.misc.urls')),
    #(r'^scriptr/', include('leeps_website.scriptr.urls')),
    #(r'^fire/', include('leeps_website.fire.urls')),

    # admin
    (r'^admin/(.*)', admin.site.root),

    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

urlpatterns += patterns('django.views.generic.simple',
    # simple redirect
    ('^$', 'redirect_to', {'url': '/home/'}),
    (r'^calendar/$', 'redirect_to', {'url': 'http://econlab.ucsc.edu/public/show_calendar.php'}),
)

if settings.DEVEL:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
