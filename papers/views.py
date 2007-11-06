from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *

# Create your views here.
def index(request):
    papers = Paper.objects.all()
    return render_to_response('papers/index.html',
        { 'papers': papers, },
        context_instance=RequestContext(request))
        
def by_title(request):
    papers = Paper.objects.all()
    papers = list(papers)
    papers.sort(key=lambda x: x.title)
    return render_to_response('papers/index.html',
        { 'papers': papers, },
        context_instance=RequestContext(request))

def by_date(request):
    papers = Paper.objects.all()
    papers = list(papers)
    papers.sort(key=lambda x: x.date)
    return render_to_response('papers/index.html',
        { 'papers': papers, },
        context_instance=RequestContext(request))
