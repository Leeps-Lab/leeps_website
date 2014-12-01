import os
import sys
sys.path.append("/var/www")

os.environ['DJANGO_SETTINGS_MODULE'] = 'leeps_website.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
