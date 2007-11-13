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
        
def by_name(request):
    projects = Project.objects.all()
    projects = list(projects)
    projects.sort(key=lambda x: x.title)
    return render_to_response('projects/index.html',
        { 'projects' : projects },
        context_instance=RequestContext(request))
        
def by_date(request):
    projects = Project.objects.all()
    projects = list(projects)
    projects.sort(key=lambda x: x.start_date)
    return render_to_response('projects/index.html',
        { 'projects' : projects },
        context_instance=RequestContext(request))
        
def by_grant(request):
    projects = Project.objects.all()
    projects = list(projects)
    projects.sort(key=lambda x: x.grant)
    return render_to_response('projects/index.html',
        { 'projects' : projects },
        context_instance=RequestContext(request))
        
def get_paper(request):
    if request.POST:
        query = request['name'].split('_')
        project = query[0]
        paper = query[1]
        project = Project.objects.get(title=project)
        paper = Paper.objects.get(title=paper)
        password = request['password']
        if password == project.password:
            if len(query) == 3:
                if query[2] == 'data':
                    url = paper.get_data_url()
                elif query[2] == 'code':
                    url = paper.get_code_url()
            else:
                url = paper.get_paper_url()
            return HttpResponse(url)
        return HttpResponse('error')
