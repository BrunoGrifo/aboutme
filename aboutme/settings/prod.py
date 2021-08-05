from aboutme.settings.base import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = json.loads(os.environ.get('ALLOWED_HOSTS'))
 
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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATIC_ROOT = os.path.join(BASE_DIR_STATIC, 'dist')

# MERDIA_ROOT = os.path.join(BASE_DIR_STATIC, 'dist')

# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
