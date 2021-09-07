from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = "backoffice"
urlpatterns = [
    path('', views.index),
    path('media/files/BrunoGrifo.pdf', views.Resume.as_view(), name="Resume"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
