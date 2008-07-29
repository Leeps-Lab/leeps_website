from django.db import models
from django.db.models import permalink
from leeps_website.people.models import Person

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=100)
    page = models.TextField()
    professor = models.ForeignKey(Person, blank=True, null=True)
    
    slug = models.SlugField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/classes/%s' % self.slug
        
    class Meta:
        verbose_name_plural = 'Classes'
    
    class Admin:
        pass
        
class Reading(models.Model):
    title = models.CharField(max_length=100, core=True)
    date = models.DateField(core=True)
    description = models.TextField(core=True)
    download = models.FileField(upload_to='readings/', core=True)
    cls = models.ForeignKey(Class, edit_inline=True, core=True)
    tag = models.CharField(max_length=100, blank=True, core=True)

    def __str__(self):
        return self.title

    class Admin:
        pass

    class Meta:
        ordering=('-date',)
