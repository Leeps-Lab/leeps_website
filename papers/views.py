from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *

# Create your views here.
def index(request):
    papers = list(Paper.objects.all())
    papers.sort(key=lambda x: x.date, reverse=True)
    return render_to_response('papers/base.html',
            { 'papers': papers, 'order': 'desc', 'keywords' : get_keywords(), 'authors' : get_authors() },
        context_instance=RequestContext(request))
        
def sort_by_date(request, order):
    papers = Paper.objects.all()
    papers = list(papers)
    if order == 'asc':
        papers.sort(key=lambda x: x.date)
    elif order == 'desc':
        papers.sort(key=lambda x: x.date, reverse=True)
    return render_to_response('papers/base.html',
        { 'papers': papers, 'order': order, 'keywords' : get_keywords(), 'authors' : get_authors() },
        context_instance=RequestContext(request))

def filter_by_author(request):
    author = request.REQUEST["author"]
    if author == "any":
        author = ""
    papers = list(Paper.objects.filter(authors__slug__icontains=author))
    papers.sort(key=lambda x: x.date, reverse=True)
    return render_to_response('papers/base.html',
            { 'papers': papers, 'order': 'desc', 'keywords' : get_keywords(), 'authors': get_authors(selected=author) },
        context_instance=RequestContext(request))

def filter_by_keyword(request):
    keyword = request.REQUEST["keyword"]
    if keyword == "Any":
        keyword = ""
    papers = list(Paper.objects.filter(keywords__icontains=keyword))
    papers.sort(key=lambda x: x.date, reverse=True)
    return render_to_response('papers/base.html',
            { 'papers': papers, 'order': 'desc', 'keywords' : get_keywords(selected=keyword), 'authors' : get_authors()},
        context_instance=RequestContext(request))

def get_keywords(selected="Any"):
    keys = set()
    for paper in Paper.objects.all():
        keys.update(paper.keywords.split(","))
    keys = list(keys)
    selecteds = []
    for key in keys:
        if key == selected:
            selecteds.append(True)
        else:
            selecteds.append(False)
    keys[0] = "Any"
    selecteds[0] = selected == "Any"
    return zip(keys, selecteds)

def get_authors(selected="any"):
    authors = set()
    for paper in Paper.objects.all():
        authors.update(paper.authors.all())
    authors = list(authors)
    selecteds = []
    for author in authors:
        if author.slug == selected:
            selecteds.append(True)
        else:
            selecteds.append(False)
    authors.insert(0,{"slug":"any","name":"Any"})
    selecteds.insert(0, selected=="any")
    return zip(authors, selecteds)

