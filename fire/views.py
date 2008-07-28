from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.conf import settings

from leeps_website.fire.models import *

# Create your views here.
def new_session(request):
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            kindling = form.cleaned_data["kindling"]
            configuration = form.cleaned_data["configuration"]
            return render_to_response('fire/session.html',
                    context_instance=RequestContext(request))
    else:
        form = SessionForm()
    return render_to_response('fire/new_session.html',
            {'form': form },
            context_instance=RequestContext(request))
