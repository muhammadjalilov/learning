import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.beat_schedule = {
    "send-notification": {
        "task": "apps.students.tasks.send_notification_for_expired_subscriptions",
        "schedule": crontab(minute=11, hour=15),
    }, }
# Load task modules from all registered Django apps.
app.autodiscover_tasks()
broker_connection_retry_on_startup = True
