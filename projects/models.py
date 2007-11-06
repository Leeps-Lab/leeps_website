from django.db import models
from leeps_website.people.models import Person
from leeps_website.papers.models import Paper

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    people = models.ManyToManyField(Person)
    grant = models.ForeignKey('Grant', blank=True, null=True)
    description = models.TextField()
    papers = models.ManyToManyField(Paper, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    class Admin:
        pass
    
class Grant(models.Model):
    grant_id = models.CharField(max_length=30)
        
    def __str__(self):
        return self.grant_id
        
    class Admin:
        pass
