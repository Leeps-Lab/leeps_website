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
    classes = person.class_set.all()
    papers = person.paper_set.all()
    return render_to_response('people/details.html',
        { 'person': person, 'classes':classes, 'papers': papers, },
        context_instance=RequestContext(request))
        
def category(request, category):
    if category == "faculty-staff":
        faculty = get_object_or_404(Category, name='faculty')
        staff = get_object_or_404(Category, name='staff')
        people = list(Person.objects.filter(category=faculty))
        people += list(Person.objects.filter(category=staff))
    else:
        category = get_object_or_404(Category, name=category)
        people = list(Person.objects.filter(category=category))
    people.sort(key=lambda person: person.name.split(" ")[-1])
    return render_to_response('people/category.html',
        { 'category': category,
          'people' : people,
        },
        context_instance=RequestContext(request))
