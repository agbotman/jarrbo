"""
Django settings for jarrbo project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# URL prefix for static files.
STATIC_URL = '/static/'
# Location of static files on server
STATIC_ROOT = '/var/www/jarrbo/static'

# URL prefix for media files
MEDIA_URL = '/media/'
# Location of media files on server
MEDIA_ROOT = '/var/www/jarrbo/media'

# Load the local and secret settings
import json
local_settings = BASE_DIR / 'local_settings.json'
f = open(local_settings)
LOCALS = json.load(f)
f.close()

SECRET_KEY = LOCALS['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = LOCALS['ALLOWED_HOSTS']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',  # to add human touch of data
    'django_filters',  # for filtering view in django_contributie

    # internal packages
    'jarrbo_theme',   # css extensions
    'jarrbo_contributie',    # contributie applicatie
    'jarrbo_profile',
    'jarrbo_auth',

    'crispy_forms',   # easy control of django forms
    'crispy_bootstrap4', # bootstrap4 support for crispy_forms
    'extra_views',    # support for extra classbased views (e.g. formsets)
    'solo',           # django_solo implements the singleton pattern
    'rosetta',        # for easy translation
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jarrbo.urls'

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

WSGI_APPLICATION = 'jarrbo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': LOCALS.get('DB_PORT') or 5432,
        'NAME': LOCALS['DB_NAME'],
        'USER': LOCALS['DB_USER'],
        'PASSWORD': LOCALS['DB_PASSWORD'] ,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#To ensure SSL requests are properly working with nginx proxying the requests to localhost
#https://stackoverflow.com/questions/41483068/djangos-httpresponseredirect-is-http-instead-of-https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Refer to the custom User model in jarrbo_auth
# This model uses the email address as unique identifiable field
AUTH_USER_MODEL = 'jarrbo_auth.User'

# Settings for django-registration
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window;

# Settings for django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4' 

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'nl'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True
# USE_L10N = True   deprecation warning Django 4.2
USE_TZ = True

USE_THOUSAND_SEPARATOR = True

LOGIN_URL = '/auth/login/'
# URL where requests are redirected after login when contrib.auth.login view gets no next parameter
LOGIN_REDIRECT_URL = '/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REMOTE_BACKUP = Path(LOCALS['REMOTE_BACKUP'])
DATA_FOLDER = Path(LOCALS['DATA_FOLDER'])
