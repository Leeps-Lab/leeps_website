from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.conf import settings
from leeps_website.scriptr.models import Script
from leeps_website.scriptr.forms import RunScriptForm
import uuid, os

# Create your views here.
def index(request):
    return render_to_response('scriptr/index.html',
            {'scripts': Script.objects.all()},
            context_instance=RequestContext(request))
        
def details(request, slug):
    script = get_object_or_404(Script, pk=slug)
    examples = script.example_set.all()
    
    if request.method == 'POST':
        form = RunScriptForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            output_type = form.cleaned_data['output_type']
            output = script.execute(input, output_type)
            url = settings.MEDIA_URL+'/'+'scriptr'+'/'+os.path.split(output)[1].replace(' ', '%20')
            print url
            return HttpResponseRedirect(url)
    else:
        form = RunScriptForm()
    return render_to_response('scriptr/details.html',
            { 'script': script,
              'examples': examples,
              'form': form },
            context_instance=RequestContext(request))
