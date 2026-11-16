# C:\skillscontinua\skillscontinua_core\settings.py
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-skillscontinua-secret-key-2026-very-long-and-secure')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    'skillscontinua.com',
    'www.skillscontinua.com',
    'app.skillscontinua.com',
    'skillscontinua-1.onrender.com',
    '127.0.0.1',
    'localhost',
    '*',
]

CSRF_TRUSTED_ORIGINS = [
    'https://skillscontinua.com',
    'https://www.skillscontinua.com',
    'https://app.skillscontinua.com',
    'https://skillscontinua-1.onrender.com',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'accounts',
    'courses',
    'certifications',
    'vocational',
    'village',
    'crispy_forms',
    'crispy_bootstrap5',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'skillscontinua_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'skillscontinua_core.wsgi.application'


# Database
# Supports local SQLite development and dynamic PostgreSQL production toggling
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Optional override if DATABASE_URL environment variable is provided
database_url = os.getenv('DATABASE_URL')
if database_url:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(default=database_url, conn_max_age=600)


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

# Crispy Forms Bootstrap 5 Integration
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'

# Authentication Redirection
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/dashboard/'
LOGOUT_REDIRECT_URL = '/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'