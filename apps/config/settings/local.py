from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_celery_beat',
    'django_celery_results',
]

result_backend = 'django-db'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# DJANGO_CELERY_BEAT_TZ_AWARE = False
# CELERY_ENABLE_UTC = False
