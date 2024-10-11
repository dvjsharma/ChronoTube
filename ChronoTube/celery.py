from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging.config
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChronoTube.settings')

app = Celery('ChronoTube')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks in registered Django apps
app.autodiscover_tasks()

# Use Django's database-backed scheduler for Celery beat
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# Configure logging
logging.config.dictConfig(settings.LOGGING)