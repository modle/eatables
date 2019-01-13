import os

assert 'DATABASE_URL' in os.environ, 'Set DATABASE_URL in your env!'
assert 'SECRET_KEY' in os.environ, 'Set SECRET_KEY in your env!'
DEBUG = False
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

ALLOWED_HOSTS = []
