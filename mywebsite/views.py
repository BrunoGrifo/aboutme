from django.http import response
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.views import View


# Create your views here.

def index(request):
    return render(request, 'homepage.html')


class Resume(View):

    http_method_names = ["get", "post"]


    def get(self, request, *args, **kwargs):
        f = open(settings.MEDIA_URL+'files/BrunoGrifo.pdf', "rb").read()
        response = HttpResponse(FileWrapper(f), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=brunogrifo.pdf'
        f.close()
        return response

        # f = open(settings.MEDIA_URL+'files/BrunoGrifo.pdf', 'rb').read()
        # return HttpResponse(f, mimetype='application/pdf')


    # def post(self, request, pk, *args, **kwargs):
    #     return 