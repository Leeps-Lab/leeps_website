from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *
from people.models import *
# Create your views here.

def index(request):
    classes = Class.objects.all()
    return render_to_response('classes/index.html',
        { 'classes': classes, },
        context_instance=RequestContext(request))

def details(request, class_name):
    cls = get_object_or_404(Class, slug=class_name)
    readings = Reading.objects.filter(cls=cls)
    return render_to_response('classes/details.html',
        { 'class': cls, 'readings': readings, },
        context_instance=RequestContext(request))
