from .base import *

DEBUG = FALSE

ALLOWED_HOST = ['django.illu.arcturus.uberspace.de',]

STATIC_ROOT = os.path.abspath(
    os.path.join(BASE_DIR,
    '/var/www/virtual/illu/django.illu.arcturus.uberspace.de/static')
)

# Gunicorn
USE_X_FORWARDED_HOST =TRUE
