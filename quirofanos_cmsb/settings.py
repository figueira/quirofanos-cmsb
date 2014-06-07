"""
Django settings for quirofanos_cmsb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%hx_qp%(r5qd1jz$n&ind0i7^(c4ac2y#*zb95)nc6al#m_lku'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'autenticacion',
    'plan_quirurgico',
    'medico',
    'coordinador',
    'jefe',
    'quirofanos_cmsb',
    'south',
    'widget_tweaks',
    'dajaxice',
    )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

ROOT_URLCONF = 'quirofanos_cmsb.urls'

WSGI_APPLICATION = 'quirofanos_cmsb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'quirofanos_cmsb',
'USER': 'quirofanos_cmsb',
'PASSWORD': 'cmsb',
'HOST': '127.0.0.1',
'PORT': '5432',
}
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/luisincrespo/usb/taller_desarrollo_software/quirofanos_cmsb/static/collecstatic/'

MEDIA_ROOT = '/home/luisincrespo/usb/taller_desarrollo_software/quirofanos_cmsb/static/media/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

# Templates

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Template Loaders

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

# Flash Message Tags - Compatibilidad con Bootstrap

from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
message_constants.INFO: 'info',
message_constants.SUCCESS: 'success',
message_constants.WARNING: 'warning',
message_constants.ERROR: 'danger',
}

# Procesadores de Contexto en Templates

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "quirofanos_cmsb.helpers.custom_processors.constantes_texto",
    )

# Authentication Backends

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    )

# Authentication Profile Module

AUTH_PROFILE_MODULE = 'quirofanos_cmsb.Cuenta'

# Login URL

LOGIN_URL = 'inicio'

# Email Dummy Backend (Quitar en Produccion y Colocar la Configuracion para Utilizar el SMTP de Gmail)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
