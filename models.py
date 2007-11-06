from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    
    class Admin():
        pass
        
    def __str__(self):
        return self.name
