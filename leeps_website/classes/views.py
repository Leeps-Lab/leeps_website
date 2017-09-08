from django.http import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from leeps_website.people.models import *
# Create your views here.

def index(request):
    classes = Class.objects.all()
    return render(request,
        'classes/index.html',
        { 'classes': classes, })

def details(request, class_name):
    cls = get_object_or_404(Class, slug=class_name)
    readings = Reading.objects.filter(cls=cls)
    tags = set(["All"])
    for reading in readings:
        if reading.tag != None:
            tags.add(reading.tag)
    return render(request,
            'classes/details.html',
            { 'class': cls, 'readings': readings, 'tags': tags})

def get_readings_by_tag(request, class_name, tag_name):
    cls = get_object_or_404(Class, slug=class_name)
    readings = Reading.objects.filter(cls=cls)
    tags = {}
    for reading in readings:
        tags[reading.tag] = ""
    if None in tags:
        del tags[None]
    tag_name = str(tag_name)
    if tag_name.count('All') == 1:
        tagged = readings
    else:
        tagged = [reading for reading in readings if tag_name.count(str(reading.tag)) == 1]
    return render(request,
            'classes/details.html',
            { 'class': cls, 'readings': tagged, 'tags': ['All']+tags.keys()})
