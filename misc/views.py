from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from leeps_website.misc.models import *

def index(request):
    pages = Page.objects.all()
    categories = Category.objects.all()
    hierarchy = {}
    for category in categories:
        hierarchy[category] = []
    for page in pages:
        hierarchy[page.category].append(page)
    return render_to_response('misc/index.html',
        { 'hierarchy': hierarchy, },
        context_instance=RequestContext(request))

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pages = Page.objects.filter(category=category)
    return render_to_response('misc/category.html',
        { 'category': category,
          'pages': pages },
        context_instance=RequestContext(request))

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render_to_response('misc/page.html',
        { 'page': page, },
        context_instance=RequestContext(request))
