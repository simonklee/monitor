import os
import logging

# server specific code
PROJECT_PATH = os.path.split(os.path.realpath(__file__))[0]
URL = 'http://mon.sedio.org'
GLOBAL_LOG_LEVEL = logging.INFO
DEBUG = True

# Admins
ADMINS = (('Simon Zimmermann', 'simonz05@gmail.com'),)
MANAGERS = ADMINS

# localization
TIME_ZONE = 'Europe/Copenhagen'
LANGUAGE_CODE = 'en'

# Urls
ROOT_URLCONF = 'monitor.urls'

# Media
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = ''.join([URL, '/media/'])
ADMIN_MEDIA_PREFIX = '/media/admin/'


# Various URL's
LOGIN_URL = '/medlem/login/'
LOGOUT_URL = '/medlem/logut/'
LOGIN_REDIRECT_URL = '/medlem/'
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Auth
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)
TEMPLATE_DEBUG = DEBUG
TEMPLATE_LOADERS = (
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.csrf",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    #"apps.mon.context_processors.sites",
    "mon.context_processors.extra",
)

# Middleware
MIDDLEWARE_CLASSES = (
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'johnny.middleware.CommittingTransactionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.databrowse',
    'django.contrib.markup',

    # external apps.
    'debug_toolbar',
    'django_extensions',
    'johnny',
    'south',
    'tabs',
    'mon',
    'apps.chart',
)
