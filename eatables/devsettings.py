import os
import urlparse

print 'loading dev settings'

DATABASE_URL = os.environ["DATABASE_URL"]

assert 'SECRET_KEY' in os.environ, 'Set SECRET_KEY in your .env file!'
SECRET_KEY = os.environ["SECRET_KEY"]

if os.environ['PLATFORM'] == 'windows':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.environ['BASE_DIR'], 'db.sqlite3'),
        }
    }
else:
    assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your .env file!'
    urlparse.uses_netloc.append("postgres")
    DATABASE_URL = urlparse.urlparse(os.environ["DATABASE_URL"])
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
DEBUG = os.environ["DEBUG"]
