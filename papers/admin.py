from django.contrib import admin
from django import forms

from models import Paper

class PaperAdmin(admin.ModelAdmin):
    filter_horizontal = ('authors',)

admin.site.register(Paper, PaperAdmin)
