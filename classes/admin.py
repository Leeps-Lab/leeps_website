
from django.contrib import admin
from django import forms

from models import Class, Reading

class ReadingInline(admin.StackedInline):
    model = Reading
    extra = 1

class ClassAdmin(admin.ModelAdmin):
    inlines = [ReadingInline]

admin.site.register(Class, ClassAdmin)
admin.site.register(Reading)
