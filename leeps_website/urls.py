from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^papers/', include('leeps_website.papers.urls')),
    url(r'^classes/', include('leeps_website.classes.urls')),
    url(r'^misc/', include('leeps_website.misc.urls')),
    url(r'^projects/', include('leeps_website.projects.urls')),
    url(r'^people/', include('leeps_website.people.urls')),

    url(r'^$', RedirectView.as_view(url='/home'))
]
