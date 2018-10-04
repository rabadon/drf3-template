#######################################
# ローカルで実行したときの設定
#######################################

import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name(dev)',
        'USER': 'db_user(dev)',
        'PASSWORD': 'db_passworddb_user(dev)',
        'HOST': 'db_hostdb_user(dev)',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
    # データベースを複数使う場合に設定 MultipleDataBase
    'dev2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

WSGI_APPLICATION = 'config.wsgi_dev.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# コピー先(公開ディレクトリ)の設定
STATIC_ROOT = BASE_DIR + '/../static_collecttest'

# ???
STATIC_URL = '/static/'

# コピー元
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

# メディアルート
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')
MEDIA_URL = 'http://localhost:8000/media/'
