from django.db import models
from django.forms import ModelForm

# Create your models here.
class Kindling(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="fire/kindlings/")

    def __str__(self):
        return self.name

class Configuration(models.Model):
    name = models.CharField(max_length=50)
    kindling = models.ForeignKey(Kindling)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="fire/configurations/")

    def __str__(self):
        return self.kindling.name + ": " + self.name

class Session(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    kindling = models.ForeignKey(Kindling)
    configuration = models.ForeignKey(Configuration)

class SessionForm(ModelForm):
    class Meta:
        model = Session

class Log(models.Model):
    name = models.CharField(max_length=50)
    data = models.TextField(blank=True)
    session = models.ForeignKey(Session)
