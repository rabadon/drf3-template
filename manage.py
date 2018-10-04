#!/usr/bin/env python
import os
import sys

import pymysql

pymysql.install_as_MySQLdb()

if __name__ == "__main__":

    # サーバーには置き換えない
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.test")
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
