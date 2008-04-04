from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.conf import settings
from leeps_website.scriptr.models import Script
from leeps_website.scriptr.forms import RunScriptFormFactory
import uuid, os

# Create your views here.
def index(request):
    return render_to_response('scriptr/index.html',
            {'scripts': Script.objects.all()},
            context_instance=RequestContext(request))
        
def run_script(request, scriptslug):
    script = get_object_or_404(Script, pk=scriptslug)
    if request.method == 'POST':
        form = RunScriptForm(request.POST)
        if form.is_valid():
            glob = {}
            loc = {}
            execfile(script.get_file_filename(), glob, loc)
            output_filename = uuid.uuid4().hex+'.png'
            output_path = os.path.join(
                    settings.WORKING_DIR, 'site_media', 'scriptr', output_filename)
            loc['main_script'](form.cleaned_data, output_path)
            return HttpResponseRedirect('/site_media/scriptr/'+output_filename)
    else:
        form = RunScriptFormFactory(script.get_file_filename())
    return render_to_response('scriptr/run_script.html',
            { 'form': form },
            context_instance=RequestContext(request))
