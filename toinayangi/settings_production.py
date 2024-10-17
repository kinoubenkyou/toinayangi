from os import environ

from toinayangi.settings import *


ALLOWED_HOSTS = environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
DEBUG = False
