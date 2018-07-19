from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTING_MODULE", 'day09.settings')

app = Celery("python03")

app.conf.CELERY_TIMEZONE = "Asia/Shanghai"

app.config_from_object("django.conf:settings")

app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
