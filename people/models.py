from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    # return our name when asked to print ourselves    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "categories"

class Person(models.Model):    
    # core fields (required)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(('A', 'Active'), ('E', 'Emeriti')))
    
    # extras (not required)
    title = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    picture = models.ImageField(blank=True, upload_to='people/images/')
    email = models.EmailField(blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='people/')
    
    # this will be the string used to form the URL
    slug = models.SlugField()
    
    # return our name when asked to print ourselves    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return '/people/%s' % self.slug
        
    class Meta:
        verbose_name_plural = "people"
