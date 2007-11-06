from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render_to_response('projects/index.html',
        { 'projects' : projects },
        context_instance=RequestContext(request))
