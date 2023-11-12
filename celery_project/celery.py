import os
from datetime import timedelta
from celery import Celery
from time import sleep
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
# have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="addition_task")
def add(x, y):
    sleep(20)
    return x + y


# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


# Method 2
# app.conf.beat_schedule = {
#     'every-10-seconds':{
#         'task':'myapp.task.clear_session_cache',
#         'schedule': 10,
#         'args':('11111', )
#     }
#     # Add more periodic tasks as needed
# }

# Method 3
# # Using timedelta
# app.conf.beat_schedule = {
#     'every-10-seconds':{
#         'task':'myapp.task.clear_session_cache',
#         'schedule': timedelta(seconds=10),
#         'args':('11111', )
#     }
#     # Add more periodic tasks as needed
# }


# Method 4

# Using crontab
app.conf.beat_schedule = {
    'every-10-seconds':{
        'task':'myapp.tasks.clear_session_cache',
        'schedule': crontab(minute= '*/1'),
        'args':('11111', )
    }
    # Add more periodic tasks as needed
}