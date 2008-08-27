from django.contrib import admin
from django import forms
from leeps_website.projects.models import Project, Grant

class ProjectAdmin(admin.ModelAdmin):
    pass

class GrantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Grant, GrantAdmin)

from leeps_website.fire.models import Kindling, Configuration, Session

class KindlingAdmin(admin.ModelAdmin):
    pass

class ConfigurationAdmin(admin.ModelAdmin):
    pass

class SessionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Kindling, KindlingAdmin)
admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Session, SessionAdmin)
    
from leeps_website.papers.models import Paper

class PaperAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paper, PaperAdmin)

from leeps_website.people.models import Person, Category

class PersonAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Category, CategoryAdmin)

from leeps_website.classes.models import Class, Reading

class ReadingAdminInline(admin.TabularInline):
    model = Reading

class ClassAdmin(admin.ModelAdmin):
    inlines = [ReadingAdminInline]

admin.site.register(Class, ClassAdmin)

from django.contrib.flatpages.models import FlatPage

class FlatPageAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = forms.Textarea(attrs={'rows' : 20, 'cols' : 100})
        return super(FlatPageAdmin, self).formfield_for_dbfield(db_field,**kwargs)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

from leeps_website.misc.models import File, Page, Category

class FileAdmin(admin.ModelAdmin):
    list_display = ('file',)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('name',)
    prepopulated_fields = {'slug': ('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display= ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(File, FileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
