from django.db import models
from django.conf import settings
import os
from uuid import uuid4 as uuid

# Create your models here.
class Script(models.Model):
    name = models.CharField(max_length=20)
    last_modified = models.DateField(auto_now=True)
    code = models.TextField()
    slug = models.SlugField(prepopulate_from=("name",), primary_key=True)
    last_output = models.CharField(max_length=200, blank=True, editable=False)
    
    def execute(self, text, output_type):
        glob = {}
        loc = {}
        code = compile(self.code.replace('\r\n', '\n'), '<string>', 'exec')
        exec(code, glob, loc)
        output_path = os.path.join(settings.MEDIA_ROOT, 'scriptr', uuid().hex+'.'+output_type)
        code = compile(text.replace('\r\n', '\n'), '<string>', 'exec')
        exec(code, glob, loc)
        loc['main_script'](loc, output_path)
        if self.last_output:
            try:
                os.remove(self.last_output)
            except OSError:
                pass
        self.last_output = output_path
        self.save()
        return self.last_output
        
    class Admin:
        pass
        
    def __str__(self):
        return self.name

class Example(models.Model):
    script = models.ForeignKey(Script, edit_inline=True)
    name = models.CharField(max_length=100)
    text = models.TextField(core=True)
    image = models.URLField(blank=True, editable=False)
    
    def save(self):
        image = self.script.execute(self.text)
        os.rename(image, os.path.join(os.path.split(image)[0], self.name+'.png'))
        self.image = settings.MEDIA_URL+'/'+'scriptr'+'/'+self.name+'.png'.replace(' ', '%20')
        super(Example, self).save()
