from django.conf.urls import url
from .views import *
from django.views.generic import RedirectView

urlpatterns = [
    url(r'details/(?P<person>[\w-]+)', details),
    url(r'(?P<category>[\w-]+)', category),
    url(r'^$', RedirectView.as_view(url='/people/faculty'))
]
