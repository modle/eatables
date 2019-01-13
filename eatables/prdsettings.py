import os
import urllib.parse

urlparse.uses_netloc.append("postgres")

assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your env!'
DATABASE_URL = urlparse.urlparse(os.environ["DATABASE_URL"])

assert 'SECRET_KEY' in os.environ, 'Set SECRET_KEY in your env!'
SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_URL.path[1:],
        'USER': DATABASE_URL.username,
        'PASSWORD': DATABASE_URL.password,
        'HOST': DATABASE_URL.hostname,
        'PORT': DATABASE_URL.port
    }
}

DEBUG = False

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
