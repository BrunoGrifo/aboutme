from django.contrib import admin
from grifo_utils.os.system import _delete_file

from .models import *
# Register your models here.


def delete_content_model(modeladmin, request, queryset):
    for contentmultimediafile in queryset:
        _delete_file(contentmultimediafile.file_upload.path)
        contentmultimediafile.delete()

@admin.register(ContentMultimediaFile)
class ContentClean(admin.ModelAdmin):
    actions = [delete_content_model]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


def delete_paragraph_model(modeladmin, request, queryset):
    for paragraph in queryset:
        if paragraph.content:
            _delete_file(paragraph.content.file_upload.path)
            paragraph.content.delete()
        paragraph.delete()

@admin.register(Paragraph)
class ParagraphClean(admin.ModelAdmin):
    actions = [delete_paragraph_model]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


def delete_project_model(modeladmin, request, queryset):
    for project in queryset:
        for paragraph in project.paragraph_set.all():
            if paragraph.content:
                _delete_file(paragraph.content.file_upload.path)
                paragraph.content.delete()
            paragraph.delete()
        project.delete()

@admin.register(Project)
class ProjectClean(admin.ModelAdmin):
    actions = [delete_project_model]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False




admin.site.register(Tag)
#admin.site.register(Project)
#admin.site.register(Paragraph)
admin.site.register(ContentMultimediaFileType)
#admin.site.register(ContentMultimediaFile, ContentClean)