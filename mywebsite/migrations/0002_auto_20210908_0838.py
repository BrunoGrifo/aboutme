# Generated by Django 3.1.7 on 2021-09-08 08:38

import django.core.files.storage
from django.db import migrations, models
import grifo_utils.paths.validators
import mywebsite.models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contentmultimediafile',
            old_name='file_thumb',
            new_name='file_name',
        ),
        migrations.AlterField(
            model_name='contentmultimediafile',
            name='file_upload',
            field=models.FileField(default='default/', max_length=500, storage=django.core.files.storage.FileSystemStorage(location='/Users/brunogrifo/Documents/bgrifo/aboutme/aboutme/media'), upload_to=mywebsite.models.get_upload_path_pp, validators=[grifo_utils.paths.validators.FileValidator(content_types=('video/mp4', 'video/mpeg', 'video/quicktime', 'video/webm', 'video/x-ms-wmv', 'image/jpeg', 'image/jpg', 'image/png', 'image/gif'), max_size=20971520)]),
        ),
    ]
