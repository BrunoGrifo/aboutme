from aboutme.settings.base import *

#override and customize settings


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2#^i%oy_8mu-+u968#c=wupq5^nk=-a0*xu6a$bz7a(+a8^s(*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aboutme',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR_STATIC, 'dist'),
# )
# STATIC_ROOT = os.path.join(BASE_DIR_STATIC, 'static')


# # ----------------------
# # MEDIA CONFIGURATION
# # ----------------------


# MEDIA_ROOT = os.path.join(BASE_DIR_STATIC, 'media')
# MEDIA_URL = '/media/'

#não faço a minima ideia do que meter aqui
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'



# AWS_ACCESS_KEY_ID = ""
# AWS_SECRET_ACCESS_KEY = ""
# AWS_STORAGE_BUCKET_NAME = ""
# AWS_S3_CUSTOM_DOMAIN = ""
# AWS_DEFAULT_ACL = 'public-read'

# AWS_LOCATION = 'static'
# STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)


# AWS_S3_FILE_OVERWRITE = False
# DEFAULT_FILE_STORAGE = 'aboutme.storages.MediaStore'


# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR_STATIC, 'dist'),
# )
# STATIC_ROOT = os.path.join(BASE_DIR_STATIC, 'static')


# MEDIA_FOLDER = 'https://{}/media/'.format(AWS_S3_CUSTOM_DOMAIN)

