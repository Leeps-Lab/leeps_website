from django.contrib import admin
from django import forms

from models import Project, Grant

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('people','papers')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Grant)

