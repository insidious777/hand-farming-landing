"""
Django settings for hand_farming_landing project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

from django.utils.translation import gettext_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k8us=n*-b=7rvvvz6xl1m(&mr#7jnpza9x_p8s#ti09w!d#d8$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['83b713b76353.ngrok.io', 'localhost', '127.0.0.1', 'handfarming.com.ua', 'www.handfarming.com.ua']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rosetta',
    'ckeditor',
    'ckeditor_uploader',
    'main_page',
    'news',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hand_farming_landing.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'hand_farming_landing.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('uk', gettext_lazy('Ukrainian')),
    ('en', gettext_lazy('English')),
    ('ru', gettext_lazy('Russian')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

ROSETTA_SHOW_AT_ADMIN_PANEL = False

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static_root'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media_root'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'noreply@handfarming.com'

# must be tuple with two items: language code and email
# example: ('uk', 'myemail@gmail.com')
NOTIFY_NEW_FEEDBACK_EMAILS = [('uk', 'test@gmail.com')]

CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'office2013',
        'toolbar': 'full',
        'extraPlugins': 'lineheight',
        'removeButtons': 'Save,NewPage,ExportPdf,Templates,SelectAll,Form,HiddenField,Checkbox,Radio,TextField,Textarea,Select,Button,ImageButton,Flash,Smiley,Anchor,Unlink,BidiLtr,BidiRtl,Language',
        'toolbarGroups': [
            {
                'name': 'document',
                'groups': ['mode', 'document', 'doctools']
            },
            {
                'name': 'clipboard',
                'groups': ['undo', 'clipboard']
            },
            {
                'name': 'editing',
                'groups': ['spellchecker', 'find', 'selection', 'editing']
            },
            {
                'name': 'forms',
                'groups': ['forms']
            },
            {
                'name': 'styles',
                'groups': ['styles', 'lineheight']
            },
            {
                'name': 'basicstyles',
                'groups': ['basicstyles', 'cleanup']
            },
            {
                'name': 'colors',
                'groups': ['colors']
            },
            {
                'name': 'paragraph',
                'groups': ['list', 'indent', 'blocks', 'align', 'bidi', 'paragraph']
            },
            {
                'name': 'insert',
                'groups': ['insert']
            },
            {
                'name': 'links',
                'groups': ['links']
            },
            {
                'name': 'tools',
                'groups': ['tools']
            },
            {
                'name': 'others',
                'groups': ['others']
            },
            {
                'name': 'about',
                'groups': ['about']
            }
        ],
    },
}

# NOTE: pass string values (because if you pass entire None, then it will render as empty string)
DEFAULT_EMPTY_TEXT_VALUE = ''
# This value passes to image source url (e.g. "src" attribute), titles and alt's
# image will be displayed if valid url provided else will be displayed as alt
DEFAULT_EMPTY_IMAGE_VALUE = ''
DEFAULT_EMPTY_LINK_VALUE = ''

MAIN_PAGE_STORIES_COUNT = 20

NEWS_LIST_PAGINATE_BY = 5
