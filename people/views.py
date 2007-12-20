from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *
from papers.models import Paper

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
    print person
    person = get_object_or_404(Person, slug=person)    
    papers = Paper.objects.filter(authors=person)
    return render_to_response('people/details.html',
        { 'person': person, 'papers': papers, },
        context_instance=RequestContext(request))
