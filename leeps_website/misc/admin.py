from django.contrib import admin
from django import forms

from .models import File, Page, Category

admin.site.register(File)
admin.site.register(Page)
admin.site.register(Category)

