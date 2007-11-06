from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *

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
