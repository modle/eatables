"""
Django settings for eatables project.
"""
import os
import platform
import environ
import urllib.parse

# read the eatables/.env file
environ.Env.read_env()

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') if ENVIRONMENT == 'prod' else []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_static_jquery',
    'markdown_deux',
    'menu',
    'gunicorn',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'eatables.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eatables.wsgi.application'

# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static file sources (CSS, JavaScript, Images)
# this is what gets served; these are stored in the server app dir; where the hell is this? There are about 450 files
# a dir gets created with the name defined in STATIC_SOURCE
STATIC_ROOT = 'staticfiles'
# STATIC_ROOT = os.path.join(os.environ['BASE_DIR'], STATIC_SOURCE)

# see static in urls.py; STATIC_URL points to STATIC_ROOT
STATIC_URL = '/staticfiles/'

# the location static files get copied from with collectstatic
# STATIC_SOURCE varies by environment; heroku BASE_DIR returns a path with 1 less /eatables/ in it
os.environ['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
assert 'BASE_DIR' in os.environ, 'BASE_DIR is not defined in the environment; check settings.py'
STATIC_SOURCE = 'static'
STATICFILES_DIRS = [
    os.path.join(os.environ['BASE_DIR'], STATIC_SOURCE),
]

MEDIA_ROOT = os.path.join(os.environ['BASE_DIR'], 'eatables')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/accounts/loggedin/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.environ['BASE_DIR'], 'db.sqlite3'),
    }
}

if 'DATABASE_URL' in os.environ:
    urllib.parse.uses_netloc.append("postgres")
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

SECRET_KEY = os.environ.get('SECRET_KEY', 'badkeyisbad')

# verify environment-specific settings
if os.environ.get('ENVIRONMENT', '') == 'prod':
    assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your env!'

