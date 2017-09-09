import os
import urlparse

print 'loading prd settings'

urlparse.uses_netloc.append("postgres")
assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your .env file!'
DATABASE_URL = urlparse.urlparse(os.environ["DATABASE_URL"])

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

DEBUG = os.environ["DEBUG"]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
