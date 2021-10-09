# 1. Imports
import environ

from .base import *


env = environ.Env()

environ.Env.read_env()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG', cast=bool)

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DBNAME'),
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPASSWORD'),
        'HOST': env('DBHOST'),
        'PORT': '',
    }
}