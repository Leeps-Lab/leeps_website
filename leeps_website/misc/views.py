from django.http import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from .models import *

def index(request):
    pages = Page.objects.all()
    categories = Category.objects.all()
    hierarchy = {}
    for category in categories:
        hierarchy[category] = []
    for page in pages:
        hierarchy[page.category].append(page)
    return render(request,
        'misc/index.html',
        { 'hierarchy': hierarchy, })

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pages = Page.objects.filter(category=category)
    return render(request,
        'misc/category.html',
        { 'category': category,
          'pages': pages })

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request,
        'misc/page.html',
        { 'page': page, })
