#######################################
# テスト環境で実行したときの設定
#######################################


import os

from .base import * # ベースの設定を読み込み

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name(test)',
        'USER': 'db_user(test)',
        'PASSWORD': 'db_password(test)',
        'HOST': 'db_host(test)',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

WSGI_APPLICATION = 'config.wsgi_test.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# コピー先(公開ディレクトリ)の設定
STATIC_ROOT = '/var/www/html/static/' + PROJECT_NAME + '/django'

# 見る先
STATIC_URL = '/static/lolreported/django/'

# コピー元
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)
