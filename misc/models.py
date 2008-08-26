from django.db import models
from django.utils.html import escape
from leeps_website.settings import MEDIA_ROOT
import os

def file_saver(instance, filename):
    if instance.file:
        os.unlink(instance.file.path)
    return MEDIA_ROOT + '/misc/' + filename

# Create your models here.
file_help_text =\
        '<p class="help">'+\
        'Files can be linked in a Markdown document with '+\
        '[&lt;link-text&gt;](/site_media/&lt;filename&gt;).'+\
        '</p><p class="help">'+\
        'Or accessed directly at http://leeps.ucsc.edu/site_media/misc/&lt;filename&gt;.'+\
        '</p>'
class File(models.Model):
    file = models.FileField(upload_to=file_saver, help_text=file_help_text)
