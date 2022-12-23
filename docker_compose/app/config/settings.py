import os
from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include
import logging.config

load_dotenv()
include(
    'components/log_conf.py',
    'components/application_definition.py',
    'components/database.py',
    'components/password_validation.py',
)

logging.config.dictConfig(log_conf)

root = logging.getLogger()

DEBUG = os.environ.get('DEBUG', False)
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')
LOCALE_PATHS = ['movies/locale']

try:
    root.info("Просматриваем доступные хосты Django.")
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')
    ALLOWED_HOSTS = [] if not any(ALLOWED_HOSTS) else ALLOWED_HOSTS
    print(ALLOWED_HOSTS)
except AttributeError:
    root.error("В доступных хостах ничего нет, Django не запуститься.")

INTERNAL_IPS = [
    "127.0.0.1",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'data'],
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

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'apps.core.pagination.StandardResultsSetPagination'
}
WSGI_APPLICATION = 'config.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
