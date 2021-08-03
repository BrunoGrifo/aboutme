from aboutme.settings.base import *
import json

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = json.loads(os.environ.get('ALLOWED_HOSTS'))





