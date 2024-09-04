"""
Django settings for EtransDjango project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from decouple import config
from pathlib import Path
import os
import dj_database_url
import cloudinary_storage
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#  pip freeze > requirements.txt  Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(@&&^pd(0-r9s5gx5t=$()q5uzao@8)7epqjlv4u#ff-=jm%h5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app','.now.sh']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'cart',
       'orders',
    'django_extensions',
     'mathfilters',
       'wishlist',
       'django.contrib.sites',
      'allauth',
        'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
  
    "django_htmx",
    "taggit",   'blog', 
     'cloudinary_storage',
    
    'cloudinary'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
      "django_htmx.middleware.HtmxMiddleware",
       "whitenoise.middleware.WhiteNoiseMiddleware",
]
SOCIALACCOUNT_PROVIDERS = {
   
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
       
     
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    'facebook':
{'METHOD': 'oauth2',
'SCOPE': ['email','public_profile', 'user_friends'],
'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
'FIELDS': [
'id',
'email',
'name',
'first_name',
'last_name',
'verified',
'locale',
'timezone',
'link',
'gender',
'updated_time'],
'EXCHANGE_TOKEN': True,
'LOCALE_FUNC': lambda request: 'kr_KR',
'VERIFIED_EMAIL': False,
'VERSION': 'v2.4'}}


ROOT_URLCONF = 'EtransDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                      'category.context_list.menu_links', 'cart.context_processors.counter',
            ],
             "builtins": ['blog.templatetags.tag_cloud',
                         'blog.templatetags.markdown_processing', ] 
        },
    },
]

WSGI_APPLICATION = 'EtransDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL'), conn_max_age=600),
}
SITE_ID =1
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQURIED=True
LOGIN_REDIRECT_URL = "/"
SOCIALACCOUNT_LOGIN_ON_GET =True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

"""STATIC_URL = 'static/'
#STATIC_ROOT  = os.path.join(BASE_DIR, 'bestbuyproject/staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
STATICFILES_DIRS = [ 
    os.path.join('static')
]"""
STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'staticfiles']

STATIC_ROOT = BASE_DIR / 'static'

#media files
#MEDIA_URL = '/media/'

#MEDIA_ROOT = BASE_DIR/'media'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CROS_ORIGIN_ALLOW_ALL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP configuration
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'fahim1213456',
    'API_KEY': '554889398149233',
    'API_SECRET': 'xOh9Pctuw1UhBuRrj_XuP79ubbA'
}