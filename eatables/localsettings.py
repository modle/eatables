import os
import urlparse

print 'loading dev settings'

url = os.environ["DATABASE_URL"]

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
    url = env('DATABASE_URL')
    urlparse.uses_netloc.append("postgres")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port
        }
    }

assert 'DEBUG' in os.environ, 'Set DEBUG in your .env file!'
DEBUG = os.environ["DEBUG"]
