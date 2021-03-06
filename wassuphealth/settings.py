"""
Django settings for wassuphealth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import pymysql
pymysql.install_as_MySQLdb()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rc&)i4*i1(2^0=7!ujry9)eb3r9v&2w&1jbo1)et&4ja+79dc5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1',]

ROBOTS_USE_SITEMAP = False

LOGIN_URL = '/login/'

# Application definition
INSTALLED_APPS = (
	'suit',
	'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_wysiwyg',
    'debug_toolbar',
    'django.contrib.redirects',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_extensions',
	'django_comments',
	'maintenancemode',
	'taggit',
	'avatar',
	'postman',
	'postman_attachments',
	'multiupload',
	'base',
    'portal',
	'registration',
	'authentication',
    'forums',
	'profile',
	'appointments',
	'feedback',
	'QnA',
	'djconfig',
	'widget_tweaks',
	'rating'
)

MIDDLEWARE_CLASSES = (
	'djconfig.middleware.DjConfigLocMemMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
	'maintenancemode.middleware.MaintenanceModeMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# DJANGO SUIT CONFIG
SUIT_CONFIG = {
    'ADMIN_NAME': 'Wassuphealth'
}

SITE_ID = 2

ROOT_URLCONF = 'wassuphealth.urls'

WSGI_APPLICATION = 'wassuphealth.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
		'ENGINE': 'mysql.connector.django',
        'NAME': 'wassuphealth',
        'USER': 'root',
        'PASSWORD': 'root',
    	'HOST': 'localhost',
        'PORT': '8889',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# MAINTENANCE MODE
MAINTENANCE_MODE = False

# CUSTOM COMMENT APP
COMMENTS_APP = 'rating'

# USER MODEL
AUTH_USER_MODEL = 'profile.User'

# avatar
AVATAR_GRAVATAR_DEFAULT = 'mm'

# postman
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_SHOW_USER_AS = 'get_full_name'
POSTMAN_DISALLOW_MULTIRECIPIENTS = True
POSTMAN_AUTO_MODERATE_AS = True

# EMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
#EMAIL_HOST_USER = 'relay@lijianmin.me'
#EMAIL_HOST_PASSWORD = ''
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
NOTIFY_EMAIL = 'jianmin@wassuphealth.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_ROOT = '/Applications/MAMP/htdocs/wsh/images/'
MEDIA_URL = 'http://127.0.0.1:8888/wsh/images/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
DJANGO_WYSIWYG_FLAVOR = "ckeditor"

STATICFILES_DIRS = (
 '/Users/Jianmin/django_projects/healthportal/wassuphealth/media',)

TEMPLATE_DIRS = (
	"base/templates/",
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
