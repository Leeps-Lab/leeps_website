from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from models import *
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
        projects = Project.objects.filter(archived=archived)
    if order:
        try:
            projects = projects.order_by(order)
        except OperationalError:
            '''order column probably doesn't exist'''
            pass
    return render_to_response(template,
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
