from django.contrib import admin
import boto3
from django.conf import Settings, settings

from .models import *
# Register your models here.


BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME



def delete_content_model(modeladmin, request, queryset):
    s3 = boto3.client(  's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name = 'eu-west-2')
    for contentmultimediafile in queryset:
        s3.delete_object(Bucket=BUCKET_NAME, Key='media/'+str(contentmultimediafile.file_upload))
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
    s3 = boto3.client(  's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name = 'eu-west-2')
    for paragraph in queryset:
        if paragraph.content:
            s3.delete_object(Bucket=BUCKET_NAME, Key='media/'+str(paragraph.content.file_upload))
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
    s3 = boto3.client(  's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name = 'eu-west-2')
    for project in queryset:
        for paragraph in project.paragraph_set.all():
            if paragraph.content:
                s3.delete_object(Bucket=BUCKET_NAME, Key='media/'+str(paragraph.content.file_upload))
                paragraph.content.delete()
            paragraph.delete()
        if project.image:
            s3.delete_object(Bucket=BUCKET_NAME, Key='media/'+str(project.image.file_upload))
            project.image.delete()
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
admin.site.register(CV)
#admin.site.register(Project)
#admin.site.register(Paragraph)
admin.site.register(ContentMultimediaFileType)
#admin.site.register(ContentMultimediaFile, ContentClean)