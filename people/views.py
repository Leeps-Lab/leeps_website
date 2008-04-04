from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *
from leeps_website.papers.models import Paper
from leeps_website.classes.models import Class

# Create your views here.
def index(request):
    categories = []
    for category in Category.objects.all():
        categories.append((category, {
                'active': Person.objects.filter(category=category, status='A'),
                'emeriti': Person.objects.filter(category=category, status='E')}))
    
    return render_to_response('people/index.html',
        { 'categories': categories, },
        context_instance=RequestContext(request))
        
def details(request, person):
    person = get_object_or_404(Person, slug=person)
    classes = Class.objects.filter(professor=person)   
    papers = Paper.objects.filter(authors=person)
    return render_to_response('people/details.html',
        { 'person': person, 'classes':classes, 'papers': papers, },
        context_instance=RequestContext(request))
