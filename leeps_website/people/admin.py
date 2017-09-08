from django.contrib import admin
from django import forms

from .models import Person, Category


admin.site.register(Person)
admin.site.register(Category)
