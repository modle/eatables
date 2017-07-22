"""
Django settings for eatables project.
"""
import os
import environ
import platform
import sys

env = environ.Env(DEBUG=(bool, False),) # set default values and casting
environ.Env.read_env()

os.environ['PLATFORM'] = 'linux'
if 'CYGWIN' in platform.system():
    os.environ['PLATFORM'] = 'windows'

# how to get RUNNING_DEVSERVER true when running collectstatic locally?
# use windows for now; need to find a way to flag dev when on linux
RUNNING_DEVSERVER = (len(sys.argv) > 1 and sys.argv[1] in ['runserver']) or os.environ['PLATFORM'] == 'windows'

os.environ['BASE_DIR'] = os.path.dirname(os.path.abspath(__file__))
if RUNNING_DEVSERVER:
    os.environ['BASE_DIR'] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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


# Static files (CSS, JavaScript, Images)

# heroku uses collectstatic, which dumps static files to STATICFILES_DIRS from
STATIC_URL = '/eatables/staticfiles/'
STATICFILES_DIRS = [
    os.path.join(os.environ['BASE_DIR'], "staticfiles"),
]
STATIC_ROOT = os.path.join(os.environ['BASE_DIR'], STATIC_URL)
print 'STATICFILES_DIRS: '
print STATICFILES_DIRS
print 'BASE_DIR: ' + os.environ['BASE_DIR']
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(os.environ['BASE_DIR'], '')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/accounts/loggedin/'

if RUNNING_DEVSERVER:
    from eatables.localsettings import *
    print "you're using the local dev settings"
else:
    from eatables.prodsettings import *
