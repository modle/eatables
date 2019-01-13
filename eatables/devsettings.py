import os
import urllib.parse

urllib.parse.uses_netloc.append("postgres")

assert 'SECRET_KEY' in os.environ, 'Set SECRET_KEY in your .env file!'

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ['BASE_DIR'], 'db.sqlite3'),
    }
}

if 'DATABASE_URL' in os.environ:
    DATABASE_URL = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
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

assert 'DEBUG' in os.environ, 'Set DEBUG in your .env file!'
DEBUG = os.environ.get('DEBUG', False)
