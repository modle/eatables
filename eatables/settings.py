"""
Django settings for eatables project.
"""
import os
import environ
import platform
import sys

# read the eatables/.env file
env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env()

# get the os
os.environ['PLATFORM'] = 'linux'
if 'CYGWIN' in platform.system():
    os.environ['PLATFORM'] = 'windows'

# load environment-specific settings
# how to get RUNNING_DEVSERVER true when running collectstatic locally?
# use windows for now; need to find a way to flag dev when on linux
RUNNING_DEVSERVER = (len(sys.argv) > 1 and sys.argv[1] in ['runserver']) or os.environ['PLATFORM'] == 'windows'
print "RUNNING_DEVSERVER: " + str(RUNNING_DEVSERVER)
if RUNNING_DEVSERVER:
    os.environ['BASE_DIR'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    from eatables.localsettings import *
else:
    os.environ['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
    from eatables.prodsettings import *

assert 'BASE_DIR' in os.environ, 'BASE_DIR is not defined in the environment; check settings.py'

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

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
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

# where static files get copied from with collectstatic
STATICFILES_DIRS = [
    os.path.join(os.environ['BASE_DIR'], 'staticfiles'),
]

# debug
print "BASE_DIR: " + os.environ['BASE_DIR']
print "STATIC_ROOT: " + STATIC_ROOT
print "STATICFILES_DIRS: " + str(STATICFILES_DIRS)

MEDIA_ROOT = os.path.join(os.environ['BASE_DIR'], 'eatables')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/accounts/loggedin/'
