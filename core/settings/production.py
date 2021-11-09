import dj_database_url

from decouple import config, Csv

from .base import *

SECRET_KEY = config("SECRET_KEY")

DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

DATABASES['default'] = dj_database_url.config()
