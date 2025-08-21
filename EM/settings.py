"""
Django settings for EM project.
Updated for Django 5.x with S3 media/static storage.
"""

import os
from pathlib import Path

# ---------------------------
# Base Paths
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# Security
# ---------------------------
SECRET_KEY = 'django-insecure-ap7+x8e(e(5wk4al(twln@o1mt#6tv&mgtxd6b%1ypwd19o+%0'
DEBUG = False
ALLOWED_HOSTS = ['eventify.23sou.xyz' , '65.2.141.81']

# ---------------------------
# Applications
# ---------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tailwind',
    'auther',
    'hosts',
    'members',
    'theme',
    'django_browser_reload',
    'storages',
]

# ---------------------------
# Middleware
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

# ---------------------------
# URL Configuration
# ---------------------------
ROOT_URLCONF = 'EM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'EM.wsgi.application'

# ---------------------------
# Database
# ---------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ---------------------------
# Password Validators
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ---------------------------
# Internationalization
# ---------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ---------------------------
# Static & Media Files
# ---------------------------

MEDIA_URL = "https://sou-django-bucket.s3.ap-south-1.amazonaws.com/"
STATIC_URL = "https://sou-django-bucket.s3.ap-south-1.amazonaws.com/css/dist/"

# Tailwind
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ---------------------------
# AWS S3 Configuration
# ---------------------------
AWS_ACCESS_KEY_ID = 'AKIAZSJJINUQ3JBLAS4Z'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sou-django-bucket'
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True

# ---------------------------
# Django 5.x STORAGES system
# ---------------------------
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # for MEDIA files
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",  # for STATIC files
    },
}
