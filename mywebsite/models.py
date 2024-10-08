import os
import uuid

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from grifo_utils.paths.validators import FileValidator
from grifo_utils.db.abstract_models import BaseAbstractModel
from colorfield.fields import ColorField
from grifo_utils.os.system import _delete_file
import boto3
from django.conf import Settings, settings

BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME
s3 = boto3.client(  's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    region_name = 'eu-west-2')


def get_extension(instance, filename):
    _, extension = os.path.splitext(filename)
    return extension

def get_upload_path_pp(instance, filename):
        _, extension = os.path.splitext(filename)
        return f"files_uploaded/{uuid.uuid4()}{extension}"

def get_upload_path_file(instance, filename):
        name, extension = os.path.splitext(filename)
        return f"files/{name}{extension}"


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "db_Tag"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self): # pragma: no cover
        return str(self.name)


class Project(BaseAbstractModel):

    COLOR_CHOICES = [
        ("#19C801", "green"),
        ("#FCF900", "yellow"),
        ("#F50B0B", "red"),
        ("#0B2BF5", "blue"),
        ("#129CFF", "baby blue"),
        ("#E800D6", "purple")
    ]

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag, related_name='list_tags', editable=True)
    image = models.OneToOneField("ContentMultimediaFile", on_delete=models.SET_NULL, null=True, blank=True)
    color = ColorField(default='#129CFF')

    class Meta:
        db_table = "db_Project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self): # pragma: no cover
        return str(self.title)


class Paragraph(models.Model):
    id_name = models.CharField(max_length=120, unique=True)
    body = models.TextField(max_length=3000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.OneToOneField("ContentMultimediaFile", on_delete=models.SET_NULL, null=True, blank=True)
    


    class Meta:
        db_table = "db_Paragraph"
        verbose_name = "Paragraph"
        verbose_name_plural = "Paragraphs"

    def __str__(self): # pragma: no cover
        return str(self.id_name)

class ContentMultimediaFileType(models.Model):
    IMAGE = 1
    AUDIO = 2
    VIDEO = 3

    content_multimedia_file_type = models.CharField("Content Multimedia File Type", max_length=100)

    class Meta:
        db_table = "db_ContentMultimediaFileType"
        verbose_name = "Content Multimedia File Type"
        verbose_name_plural = "Content Multimedia File Types"

    def __str__(self): # pragma: no cover
        return str(self.content_multimedia_file_type)

class CV(BaseAbstractModel):
    file_upload = models.FileField(#torage=FileSystemStorage(location=settings.MEDIA_FOLDER),
                                    upload_to=get_upload_path_file)

    class Meta:
        db_table = "db_cv"
        verbose_name = "cv"
        verbose_name_plural = "cv"

    def save(self, *args, **kwargs):
        #_delete_file(settings.MEDIA_FOLDER+"/files/brunogrifo.pdf")
        s3.delete_object(Bucket=BUCKET_NAME, Key='media/files/brunogrifo.pdf')
        super(CV, self).save(*args, **kwargs)

class ContentMultimediaFile(BaseAbstractModel):
    file_upload = models.FileField(
        #storage=FileSystemStorage(location=settings.MEDIA_FOLDER),
        upload_to=get_upload_path_pp,
        validators=[
            FileValidator(
                max_size=1024 * 1024 * 20,
                content_types=("video/mp4", "video/mpeg", "video/quicktime", "video/webm", "video/x-ms-wmv", "image/jpeg", "image/jpg", "image/png", "image/gif"),
            )
        ],
        default="default/", max_length=500)
    file_name =  models.CharField(max_length=500, null=True, blank=True)
    content_multimedia_file_type = models.ForeignKey(ContentMultimediaFileType, on_delete=models.PROTECT)

    class Meta:
        db_table = "db_ContentMultimediaFile"
        verbose_name = "Conteúdo Multimédia"
        verbose_name_plural = "Conteúdos Multimédia"

    def save(self, *args, **kwargs):
        if self.pk is None:
            if get_extension(self, self.file_upload.name) in [".mp4", ".webm"]:
                content_type = ContentMultimediaFileType.objects.get(pk=ContentMultimediaFileType.VIDEO)
                self.content_multimedia_file_type = content_type
            if get_extension(self, self.file_upload.name) in [".jpeg", ".png", ".gif", ".jpg"]:
                content_type = ContentMultimediaFileType.objects.get(pk=ContentMultimediaFileType.IMAGE)
                self.content_multimedia_file_type = content_type
            if get_extension(self, self.file_upload.name) in [".wav", ".mp3"]:
                content_type = ContentMultimediaFileType.objects.get(pk=ContentMultimediaFileType.AUDIO)
                self.content_multimedia_file_type = content_type
        super(ContentMultimediaFile, self).save(*args, **kwargs)


    # def __str__(self): # pragma: no cover
    #     return str(self.file_upload.path)
    def __str__(self): # pragma: no cover
        return str(self.file_name)

    def __unicode__(self):
        return self.file_upload.path

    @property
    def get_path(self):
        return f"{settings.SERVER}{self.file_upload.url}"

    @property
    def isImage(self):
        return self.content_multimedia_file_type.content_multimedia_file_type == "IMAGE"

    @property
    def isVideo(self):
        return self.content_multimedia_file_type.content_multimedia_file_type == "VIDEO"
