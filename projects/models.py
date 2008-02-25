from django.db.models import *
from leeps_website.people.models import Person
from leeps_website.papers.models import Paper

# Create your models here.
class Project(Model):
    title = CharField(max_length=200)
    start_date = DateField(blank=True)
    end_date = DateField(blank=True,
        help_text='If left blank, displays as "[start date] - Present"')
    people = ManyToManyField(Person)
    grant = ForeignKey('Grant', blank=True)
    description = TextField()
    papers = ManyToManyField(Paper, blank=True)
    password = CharField(max_length=50, blank=True)
    protect_papers = CharField(max_length=10,
        choices=(('true', 'Yes'), ('false', 'No')), radio_admin=True)
    protect_data = CharField(max_length=10,
        choices=(('true', 'Yes'), ('false', 'No')), radio_admin=True)
    protect_code = CharField(max_length=10,
        choices=(('true', 'Yes'), ('false', 'No')), radio_admin=True)
    archived = BooleanField(blank=True)
    
    def __str__(self):
        return self.title
    
    class Admin:
        list_display = ('title', 'password')
    
class Grant(Model):
    grant_id = CharField(max_length=30)
        
    def __str__(self):
        return self.grant_id
        
    class Admin:
        pass
