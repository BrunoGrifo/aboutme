from aboutme.settings.base import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ["bgrifo-aboutme.herokuapp.com","www.bgrifo.com", "bgrifo.com"]
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE'),
        'HOST': os.environ.get('BD_HOST'),
        'USER': os.environ.get('BD_USER'),
        'PASSWORD': os.environ.get('BD_PASSWORD'),
        'PORT': '5432',
    }
}

#não faço a minima ideia do que meter aqui
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '{}.s3.amazonaws.com'.format(AWS_STORAGE_BUCKET_NAME)
AWS_DEFAULT_ACL = 'public-read'

AWS_LOCATION = 'static'
STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)


AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'core.storages.MediaStore'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'dist'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
