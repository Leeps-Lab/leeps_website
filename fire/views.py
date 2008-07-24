from django.http import *
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.conf import settings

from leeps_website.fire.models import *

# Create your views here.
def new_session(request):
    return render_to_response('fire/new_session.html',
            {'form': SessionForm() },
            context_instance=RequestContext(request))
