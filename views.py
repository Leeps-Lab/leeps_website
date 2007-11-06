from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *

# Create your views here.
def home(request):
    page = get_object_or_404(Page, name='Home')
    return render_to_response('home.html',
                                { 'content' : page.content },
                                context_instance=RequestContext(request))
        
def about(request):
    page = get_object_or_404(Page, name='About')
    return render_to_response('about.html',
                                { 'content' : page.content },
                                context_instance=RequestContext(request))
    
