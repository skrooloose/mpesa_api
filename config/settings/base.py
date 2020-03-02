"""
Django settings for mpesa project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8%wj-t24eji19)q!b0mwo=&!f=%9f&gui$*umjx(08+w5)!zns'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'mpesa_api.core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../../templates')]
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, 'static'))
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, 'media'))
MEDIA_UPLOAD_FOLDER = '%Y_%m_%d/'


JET_SIDE_MENU_COMPACT = True

# Safaricom Configs

# B2C (Bulk Payment) Configs
# see https://developer.safaricom.co.ke/test_credentials
# https://developer.safaricom.co.ke/b2c/apis/post/paymentrequest

#Consumer Key
MPESA_B2C_ACCESS_KEY = 'bmmI3UPlJa3pt8GqDG1Fu9D7cKy5YooF'
#Consumer Secret
MPESA_B2C_CONSUMER_SECRET = 'dee8AzvwJKNoZ3YW'
# This is the encryption of the scurity Credentials I used the Developer site to encrypt it.
B2C_SECURITY_TOKEN = 'E3Lw64xJ+/ayn1StCP9nu/ObqzgPgCf1IG6JEiubn91QOxkc4u8F0h9NdgjGHaWDHYDEaWxdxqd7uh3ZBsZCrPCm+8ckz8BX/Fqu/x0jOnKzEWwUdbdbFm+hV2q5HJY/EWIq6lnJQeCahkte0TQ6OoVzKyRIUsD4F+pkIIaMkjvqK5mcFWlZQIhoodXd9oBtlo7GWbcYNOjO1+GatYCtVgvjmfWHqI5k4PV/3zjNxvIcTmlB4Ao43fRvXwkRQsvc+8QOUDb6JDO0uF0UhAtz53QLdVmMNmldRoy/nEQ+QrKheY4PhXxnwhrIkFtzWhEG8AhWZjz/Ck4Kr6ePepNEuA=='
#InitiatorName
B2C_INITIATOR_NAME = 'testapi409'
# CommandID
B2C_COMMAND_ID = 'SalaryPayment'
#PartyA
B2C_SHORTCODE = '601409'
# this is the url where Mpesa  will post in case of a time out. Replace http://mpesa.ngrok.io/  with your url ow here this app is running
B2C_QUEUE_TIMEOUT_URL = 'http://mpesa.ngrok.io/mpesa/b2c/timeout'
# this is the url where Mpesa will post the result. Replace http://mpesa.ngrok.io/  with your url ow here this app is running
B2C_RESULT_URL = 'http://mpesa.ngrok.io/mpesa/b2c/result'
# this is the url where we post the B2C request to Mpesa. Replace this with the url you get from safaricom after you have passed the UATS
B2C_URL = 'https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest'

# C2B (Paybill) Configs
# See https://developer.safaricom.co.ke/c2b/apis/post/registerurl

#Consumer Secret
MPESA_C2B_ACCESS_KEY = 'bmmI3UPlJa3pt8GqDG1Fu9D7cKy5YooF'
# Consumer Key
MPESA_C2B_CONSUMER_SECRET = 'dee8AzvwJKNoZ3YW'
# Url for registering your paybill replace it the url you get from safaricom after you have passed the UATS
C2B_REGISTER_URL = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
#ValidationURL
# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_VALIDATE_URL = 'http://mpesa.ngrok.io/mpesa/c2b/validate'
#ConfirmationURL
# replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_CONFIRMATION_URL = 'http://mpesa.ngrok.io/mpesa/c2b/confirmation'
#ShortCode (Paybill)
C2B_SHORT_CODE = '600000'
#ResponseType
C2B_RESPONSE_TYPE = 'Completed'

# C2B (STK PUSH) Configs
# https://developer.safaricom.co.ke/lipa-na-m-pesa-online/apis/post/stkpush/v1/processrequest

# Url for sending the STK push request replace it the url you get from safaricom after you have passed the UATS
C2B_ONLINE_CHECKOUT_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
# Where the Mpesa will post the response
#replace http://mpesa.ngrok.io/ with your url ow here this app is running
C2B_ONLINE_CHECKOUT_CALLBACK_URL = 'http://mpesa.ngrok.io/mpesa/c2b/online_checkout/callback'
# TransactionType
C2B_TRANSACTION_TYPE = 'CustomerPayBillOnline'
# The Pass Key provided by Safaricom when you pass UAT's
# See https://developer.safaricom.co.ke/test_credentials
C2B_ONLINE_PASSKEY = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
# Your Paybill
C2B_ONLINE_SHORT_CODE = '174379'

# URL generate OAUTH token
# See https://developer.safaricom.co.ke/oauth/apis/get/generate-1
GENERATE_TOKEN_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


# number of seconds from the expiry we consider the token expired the token expires after an hour
# so if the token is 600 sec (10 minutes) to expiry we consider the token expired.
TOKEN_THRESHOLD = 600