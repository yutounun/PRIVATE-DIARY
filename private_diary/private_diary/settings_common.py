from distutils.log import Log
from modulefinder import LOAD_CONST
from pathlib import Path, os
from re import M
from telnetlib import AUTHENTICATION
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ce9=w7ks5hn4te#^e)^ihw9zg3jc%&#5fuldsr&4@w9p(shc-+'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account'
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

ROOT_URLCONF = 'private_diary.urls'

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

WSGI_APPLICATION = 'private_diary.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # PostgresSQL
    # get info from .env file
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'private_diary',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': ''
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = os.path.join(BASE_DIR,'static/'),

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

AUTH_USER_MODEL = 'accounts.CustomUser'

# set ID for identify sites to use django.contrib.sites used by django-allauth
SITE_ID = 1

AUTHENTICATION_BACKEND = (
    # for normal user (email authentication)
    'allauth.account.auth_backends.AuthenticationBackend',
    # for admin-site (Username authentication)
    'django.contrib.auth.backends.ModelBackend'
)

# settings to change into email authentication
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True

# verify email before signup
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

# Can logout by only ONE click on logout link
ACCOUNT_LOGOUT_ON_GET = True

ACOUNT_EMAIL_SUBJECT_PREFIX = ''

DEFAULT_FROM_EMAIL = 'admin@exmple.com'

DEBUG = True

# read media_file from this path
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# url will be like 'https://<host_name>/media/example.png'
MEDIA_URL = '/media/'

# When Loggin in, this page will lead viewer to this URL.
LOGGIN_REDIRECT_URL = 'diary:diary_list'

# for backup batch
BACKUP_PATH = 'backup/'
NUM_SAVED_BACKUP = 30