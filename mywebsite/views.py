from django.http import response
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.views import View
from django.http import FileResponse

from .models import *


# Create your views here.

def index(request):
    context = {
        "projects": Project.objects.filter(active=True)
    }
    return render(request, 'homepage.html', context)


class ProjectView(View):

    http_method_names = ["get", "post"]


    def get(self, request, pk, *args, **kwargs):
        project = Project.objects.get(id=pk)
        par_list = []
        #print(project.paragraph_set.all().order_by('id_name'))
        for pro in project.paragraph_set.all().order_by('id_name'):
            if pro.content:
                par_list.append({
                    "body": pro.body,
                    "path": pro.content.file_upload.url,
                    "type": pro.content.content_multimedia_file_type.content_multimedia_file_type
                })
            else:
                par_list.append({
                    "body": pro.body,
                    "path": None,
                    "type": None
                })

        context = {
            "project": project,
            "paragraphs": par_list
        }
        return render(request, 'post.html', context)



class Resume(View):

    http_method_names = ["get", "post"]


    def get(self, request, *args, **kwargs):
        with open(settings.MEDIA_ROOT+'/files/brunogrifo.pdf', "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=brunogrifo.pdf'
            return response 