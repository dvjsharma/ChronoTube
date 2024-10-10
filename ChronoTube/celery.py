from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChronoTube.settings')

app = Celery('ChronoTube')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# Use Django's database scheduler for Celery
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'