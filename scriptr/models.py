from django.db import models

# Create your models here.
class Script(models.Model):
    name = models.CharField(max_length=20)
    last_modified = models.DateField(auto_now=True)
    file = models.FileField(upload_to='scriptr/')
    slug = models.SlugField(prepopulate_from=("name",), primary_key=True)

    class Admin:
        pass
