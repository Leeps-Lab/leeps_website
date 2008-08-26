from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.contrib.flatpages.models import FlatPage

def index(request):
    pages = FlatPage.objects.all()
    return render_to_response('misc/index.html',
        { 'pages': pages, },
        context_instance=RequestContext(request))
