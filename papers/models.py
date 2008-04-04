from django.db import models
from leeps_website.people.models import Person

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Person)
    date = models.DateField()
    abstract = models.TextField()
    paper = models.FileField(blank=True, null=True, upload_to='papers/')
    data = models.FileField(blank=True, null=True, upload_to='papers/data/')
    code = models.FileField(blank=True, null=True, upload_to='papers/code/')
    publish = models.CharField(max_length=5,
        choices=(('true', 'Yes'), ('false', 'No')),
        radio_admin=True,
        help_text='''If "Yes", all files attached to this paper will be available for download.
                     If paper has no attached file(s), just put "No"''')

    def get_absolute_url(self):
        return '/papers/'
    
    def __str__(self):
        return self.title
        
    class Meta:
        ordering=('-date', 'title')
    
    class Admin:
        list_display=('title', 'date', 'publish')
    
