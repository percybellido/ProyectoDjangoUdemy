# SECURITY WARNING: don't run with debug turned on in production!
from .base import *
from pathlib import Path, os

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'dbempleado',
        'USER':'neunapp',
        'PASSWORD':'neunappcursopro',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS= [BASE_DIR/'static']

MEDIA_URL= '/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, "media")
