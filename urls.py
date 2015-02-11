from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.flatpages.models import FlatPage

from leeps_website.papers.models import Paper
from leeps_website.people.models import Person
from leeps_website.projects.models import Project
from leeps_website.classes.models import Class


admin.autodiscover()

sitemaps = {
    
    'papers': GenericSitemap({'queryset': Paper.objects.all()}),
    'people': GenericSitemap({'queryset': Person.objects.all()}),
    'projects': GenericSitemap({'queryset': Project.objects.all()}),
    'classes': GenericSitemap({'queryset': Class.objects.all()}),
    'flatpages': GenericSitemap({'queryset': FlatPage.objects.all()}),
}

urlpatterns = patterns('',
    # admin
    (r'^admin/', admin.site.urls),
    
    # app content
    (r'^papers/', include('leeps_website.papers.urls')),
    (r'^people/', include('leeps_website.people.urls')),
    (r'^projects/', include('leeps_website.projects.urls')),
    (r'^classes/', include('leeps_website.classes.urls')),
    (r'^misc/', include('leeps_website.misc.urls')),

    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps})
)

urlpatterns += patterns('django.views.generic.simple',
    # Employee Request System application redirect
    ('^apply', 'redirect_to', {'url': 'http://www.careercenter.ucsc.edu/ers/erspub/main.cfm?er_id=7658&jt=workstudy&action=displayER'}),
    # simple redirect
    ('^$', 'redirect_to', {'url': '/home/'}),
    (r'^calendar/$', 'redirect_to', {'url': 'http://econlab.ucsc.edu/public/show_calendar.php'}),
)

urlpatterns += staticfiles_urlpatterns()

#urlpatterns += patterns('',
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#)
