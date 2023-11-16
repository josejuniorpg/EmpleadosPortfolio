# SECURITY WARNING: don't run with debug turned on in production!
import os.path
#from django.conf import settings
from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
#todo Ver que en linux y Mac no de error de rutas al cargar static
STATICFILES_DIRS = [(BASE_DIR/'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'
# print('lA RUTA',BASE_DIR)
# print('STATICS',STATICFILES_DIRS)
# print('STATICS_URL',STATIC_URL)