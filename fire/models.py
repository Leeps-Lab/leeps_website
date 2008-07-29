from django.db import models
from django.conf import settings
from django import forms
import os

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
        return self.name

class Session(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    kindling = models.ForeignKey(Kindling)
    configuration = models.ForeignKey(Configuration)
    jnlp = models.FilePathField(path="fire/sessions/", match="*.jnlp", blank=True)
    def get_jnlp_url(self):
        return settings.MEDIA_URL+"/fire/sessions/%s" % os.path.basename(self.jnlp)
    def delete(self):
        os.remove(self.jnlp)
        super(Session, self).delete()

def create_session_form(
        data=None, init_username=None, init_password=None, init_host=None, init_kindling=None, init_configuration=None):
    class SessionForm(forms.Form):
        username = forms.CharField(max_length=50, required=False, initial=init_username)
        password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=False, initial=init_password)
        host = forms.CharField(max_length=50, required=False, initial=init_host)
        kindling = forms.ModelChoiceField(Kindling.objects.all(), initial=init_kindling)
        configuration = forms.ModelChoiceField(Configuration.objects.all(), initial=init_configuration)
    if data:
        return SessionForm(data)
    return SessionForm()

class Log(models.Model):
    name = models.CharField(max_length=50)
    data = models.TextField(blank=True)
    session = models.ForeignKey(Session)
