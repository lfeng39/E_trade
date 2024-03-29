"""
Django settings for E_trade project.

Generated by 'django-admin startproject' using Django 3.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3ecb=$i84um9$57vh=tx7dk@g1ho2emz#=@--!xsrcgrcs2ocl'

SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]
# ALLOWED_HOSTS = ['10.254.111.247', '10.254.101.127', '10.254.0.1']


# Application definition

INSTALLED_APPS = [
    'JAL',
    # 'djmoney',
    'Task',
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

ROOT_URLCONF = 'E_trade.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            # 注册range插件，range.py 放在templates文件夹下
            # 'libraries':{
            # 'range': 'templates.range',
            # }
        },
    },
]

WSGI_APPLICATION = 'E_trade.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jal',
        'USER': 'root',
        'PASSWORD': '12820839',
        'HOST': '127.0.0.1',
        'PORT': '3306'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static'),
    # os.path.join(BASE_DIR, 'range')
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



'''
send email
'''
'''
me.and.mr.leo.s@gmail.com
'''
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_SSL = True
# EMAIL_PORT = 465
# # EMAIL_USE_TLS = True
# # EMAIL_PORT = 587
# EMAIL_HOST_USER = 'me.and.mr.leo.s@gmail.com'
# EMAIL_HOST_PASSWORD = 'ncjg laji euxl fyso' # 发送邮件的邮箱密码或授权码
# EMAIL_CA_CERTS = ''  # 将这行添加并设置为空字符串
'''
me.and.mr.leo.promote@gmail.com
'''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
EMAIL_HOST_USER = 'me.and.mr.leo.promote@gmail.com'
EMAIL_HOST_PASSWORD = 'mlwr rqsl yviw jqyp' # 发送邮件的邮箱密码或授权码
EMAIL_CA_CERTS = ''  # 将这行添加并设置为空字符串
'''
sandianjiuke@163.com
'''
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.163.com' # 修改为你的 SMTP 服务器
# EMAIL_PORT = 465 # SMTP 端口
# EMAIL_USE_SSL = True
# # EMAIL_USE_TLS = True # 使用 TLS 安全连接
# EMAIL_HOST_USER = 'sandianjiuke@163.com' # 发送邮件的邮箱地址
# EMAIL_HOST_PASSWORD = 'NINLXTRXBRQHEUOC' # 发送邮件的邮箱密码或授权码


