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
    
    def __str__(self):
        return self.title
    
    class Admin:
        pass
    
