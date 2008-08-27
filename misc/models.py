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

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(help_text='All pages in this category can be accessed at /misc/category/&lt;slug&gt;')

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Page(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(help_text='Page can be accessed at /misc/page/&lt;slug&gt;')
    content = models.TextField(help_text='Markdown syntax allowed (http://daringfireball.net/projects/markdown/syntax)')
    category = models.ForeignKey(Category)
    javascript = models.TextField(blank=True)
    css = models.TextField(blank=True)

    def __str__(self):
        return self.title
