
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'base1.db',
        
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS =(os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')