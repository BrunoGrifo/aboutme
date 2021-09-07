from django.contrib import admin
from grifo_utils.os.system import _delete_file

from .models import *
# Register your models here.


def delete_model(modeladmin, request, queryset):
    for contentmultimediafile in queryset:
        _delete_file(contentmultimediafile.file_upload.path)
        contentmultimediafile.delete()

class ContentClean(admin.ModelAdmin):
    actions = [delete_model]





admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Paragraph)
admin.site.register(ContentMultimediaFileType)
admin.site.register(ContentMultimediaFile, ContentClean)