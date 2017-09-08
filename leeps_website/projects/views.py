from django.http import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from .models import *
from django.db.models import Q

# Create your views here.
def index(request, archived=None, order=None):
    if not archived:
        archived = False
        template = 'projects/index.html'
        projects = Project.objects.filter(Q(archived=archived) | Q(archived__isnull=True))
    else:
        archived = True 
        template = 'projects/archived.html'
        projects = Project.objects.filter(archived=archived).order_by('-end_date')
    if order:
        projects = projects.order_by(order)
    try:
        return render(request,
                template,
                { 'projects' : projects })
    except:
        projects = Project.objects.filter(
                Q(archived=archived) | Q(archived__isnull=True))
        return render(template,
                { 'projects' : projects })

def get_paper(request):
    if request.POST:
        query = request['name'].split('_')
    project = query[0]
    paper = query[1]
    project = Project.objects.get(title=project)
    paper = Paper.objects.get(title=paper)
    password = request['password']
    if password == project.password:
        url = ""
        if len(query) == 3:
            if query[2] == 'data':
                url = paper.data.url()
            elif query[2] == 'code':
                url = paper.code.url()
        else:
            url = paper.paper.url()
        return HttpResponse(url)
    return HttpResponse('error')
