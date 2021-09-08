from django.contrib import admin
from grifo_utils.os.system import _delete_file

from .models import *
# Register your models here.


def delete_model(modeladmin, request, queryset):
    for contentmultimediafile in queryset:
        _delete_file(contentmultimediafile.file_upload.path)
        print("tentative de delete")
        contentmultimediafile.delete()

@admin.register(ContentMultimediaFile)
class ContentClean(admin.ModelAdmin):
    actions = [delete_model]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False




admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(Paragraph)
admin.site.register(ContentMultimediaFileType)
#admin.site.register(ContentMultimediaFile, ContentClean)