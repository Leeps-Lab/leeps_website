from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.conf import settings

from leeps_website.fire.models import *
from jnlp import create_jnlp

# Create your views here.
def new_session(request, kindling=None, configuration=None):
    if request.method == "POST":
        form = create_session_form(data=request.POST)
        if form.is_valid():
            kindling = form.cleaned_data["kindling"]
            configuration = form.cleaned_data["configuration"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            host = form.cleaned_data["host"]
            session = Session(kindling=kindling, configuration=configuration)
            session.save()
            jnlp = open(settings.MEDIA_ROOT+"/fire/sessions/session_%s.jnlp" % session.id, 'w')
            jnlp.write(create_jnlp(username, password, host, kindling.get_file_url(), configuration.get_file_url()))
            jnlp.close()
            session.jnlp = jnlp.name
            session.save()
            return render_to_response('fire/session.html',
                    { "session" : session },
                    context_instance=RequestContext(request))
    else:
        form = create_session_form(init_kindling=kindling, init_configuration=configuration, init_host="econlab.ucsc.edu")
    return render_to_response('fire/new_session.html',
            {'form': form },
            context_instance=RequestContext(request))

def sessions(request):
    return render_to_response('fire/sessions.html',
            { "sessions" : Session.objects.all().order_by("-timestamp") },
            context_instance=RequestContext(request))

def experiments(request):
    return render_to_response('fire/experiments.html',
            { "kindlings" : Kindling.objects.all() },
            context_instance=RequestContext(request))
