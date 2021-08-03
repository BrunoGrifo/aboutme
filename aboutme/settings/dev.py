from aboutme.settings.base import *

#override and customize settings


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2#^i%oy_8mu-+u968#c=wupq5^nk=-a0*xu6a$bz7a(+a8^s(*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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