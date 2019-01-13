"""
Django settings for eatables project.
"""
import os
import platform
import environ

# read the eatables/.env file
environ.Env.read_env()

ALLOWED_HOSTS = []

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


# load environment-specific settings
if 'ENVIRONMENT' in os.environ.keys() and os.environ['ENVIRONMENT'] == 'prd':
    from eatables.prdsettings import *
else:
    from eatables.devsettings import *
