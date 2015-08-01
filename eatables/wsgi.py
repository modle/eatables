"""
WSGI config for eatables project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eatables.settings")

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

#Rely upon env var 'DYNO` to determine if we are
#running within Heroku


application = get_wsgi_application()
application = DjangoWhiteNoise(application)
