#######################################
# 本番環境で実行したときの設定
#######################################

import os

from .base import * # ベースの設定を読み込み

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name(production)',
        'USER': 'db_user(production)',
        'PASSWORD': 'db_password(production)',
        'HOST': 'db_host(production)',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

WSGI_APPLICATION = 'config.wsgi_prod.application'


# コピー先(公開ディレクトリ)の設定
STATIC_ROOT = '/var/www/html/dgamers.jp/django_static'

# 見る先
STATIC_URL = '/django_static/'

# コピー元
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

# メディアルート
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
MEDIA_URL = '/backend/media/'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
