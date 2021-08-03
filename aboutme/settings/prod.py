from aboutme.settings.base import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = json.loads(os.environ.get('ALLOWED_HOSTS'))
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd82shbn757f7lc',
        'HOST': 'ec2-23-23-128-222.compute-1.amazonaws.com',
        'USER': 'zfsgtcueiwbfxh',
        'PASSWORD': 'd241a941f3e657eafd93d4aa8d3d5c7a6d097d871f8ac36505bbf227b0d56ec5',
        'PORT': '5432',
    }
}


