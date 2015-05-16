# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1lfv#b%c6!187ojry=a8%4ola&^%40!s!5rz(_qoihykm=jx&6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

#*****************************CONFIGURACION************************
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# ruta del proyecto
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    BASE_DIR + '/templates',
)
MEDIA_URL = 'http://localhost:8000/media/'
MEDIA_ROOT = (BASE_DIR + '/media')

# ***********DJANGO SUIT TEMPLATE****************
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    # configuracion report builder
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    #************************************
)


# Application definition

INSTALLED_APPS = (
    'suit',
    'smart_selects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'report_builder',
    'bootstrap_themes',
    'apps.inicio',
    'apps.sedes',
    'apps.profesores',
    'apps.intervenciones',
    'apps.asistencias',
    'apps.configuraciones',
    'apps.conectividad',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SysGE.urls'

WSGI_APPLICATION = 'SysGE.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'escuela_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ES-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'static'),
)
# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'SysGE',
    'HEADER_DATE_FORMAT': 'l, j F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    'SEARCH_URL': '/admin/user',
    'SEARCH_URL': '/admin/sedes/alumno/',
     'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
        'intervenciones': 'icon-globe',
        'profesores':'icon-user',
        'sedes':'icon-time',
     },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
     #'MENU': (
    #   'sites',
    #     {'app': 'auth', 'label': 'Autorizacion','icon':'icon-lock', 'models': ('user', 'group')},
    #
    #     #{'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     #{'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
     #),

    # misc
    # 'LIST_PER_PAGE': 15
}