from django.db import models

def slugify(string):
    import re
    string = re.sub('\s+', '_', string)
    string = re.sub('[^\w.-]', '', string)
    return string.strip('_.- ').lower()

class Page(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s' % slugify(self.name)

    class Admin:
        pass
