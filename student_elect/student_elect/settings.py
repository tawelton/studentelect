"""
Django settings for student_elect project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import shutil

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a!n-=%+j5=o(rg^s79#==&+60u@%*foo+9jr_kdycz5%&mjbsp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mako_plus',
    'dashboard',
    'poll',
    'account',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django_mako_plus.RequestInitMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'student_elect.urls'

TEMPLATES = [
    {
        'NAME': 'django_mako_plus',
        'BACKEND': 'django_mako_plus.MakoTemplates',
        'OPTIONS': {
            # see the DMP documentation, "configuration options" page for available options
        },
    },
    {
        'NAME': 'django',
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

WSGI_APPLICATION = 'student_elect.wsgi.application'

AUTH_USER_MODEL = 'account.User'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'student_elect',
        'USER': 'tannerja_s_e',
        'PASSWORD': 'Studentelect!',
        'HOST': 'tannerjacobwelton.com',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # SECURITY WARNING: this next line must be commented out at deployment
    BASE_DIR,
)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# A logger for DMP
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django_mako_plus_simple': {
            'format': '%(levelname)s::DMP %(message)s'
        },
    },
    'handlers': {
        'django_mako_plus_console':{
            'class':'logging.StreamHandler',
            'formatter': 'django_mako_plus_simple'
        },
    },
    'loggers': {
        'django_mako_plus': {
            'handlers': ['django_mako_plus_console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
