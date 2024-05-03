
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['fluorescencia.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'base1.db',
        
    }
}
