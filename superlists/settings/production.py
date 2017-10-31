from .base import *

#DEBUG = False

ALLOWED_HOSTS = ['django.illu.arcturus.uberspace.de',]

STATIC_ROOT = os.path.abspath(
    os.path.join(BASE_DIR,
    '/var/www/virtual/illu/django.illu.arcturus.uberspace.de/static')
)

# Gunicorn
USE_X_FORWARDED_HOST = True
