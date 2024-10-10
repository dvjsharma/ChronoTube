from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChronoTube.settings')

app = Celery('ChronoTube')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch_latest_videos_every_10_seconds': {
        'task': 'core.tasks.fetch_latest_videos',  # Task name (function) to run
        'schedule': 10.0,                          # Run the task every 10 seconds
    },
}