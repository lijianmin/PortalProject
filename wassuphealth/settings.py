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


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rc&)i4*i1(2^0=7!ujry9)eb3r9v&2w&1jbo1)et&4ja+79dc5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ROBOTS_USE_SITEMAP = False

# Application definition

INSTALLED_APPS = (
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
    'robots',
    'base',
    'portal',
    'forums',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

SITE_ID = 2

ROOT_URLCONF = 'wassuphealth.urls'

WSGI_APPLICATION = 'wassuphealth.wsgi.application'

#CKEDITOR_UPLOAD_PATH = "uploads/"

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wassuphealth',
        'USER': 'root',
        'PASSWORD': 'root',
    	'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

DJANGO_WYSIWYG_FLAVOR = "ckeditor"
#DJANGO_WYSIWYG_MEDIA_URL = '/uploads/ckeditor/'


TEMPLATE_DIRS = (
	"/templates/",
)

