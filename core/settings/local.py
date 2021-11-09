# 1. Imports
from decouple import config
from decouple import Csv

from .base import *


SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DBNAME'),
        'USER': config('DBUSER'),
        'PASSWORD': config('DBPASSWORD'),
        'HOST': config('DBHOST'),
        'PORT': '',
    }
}
