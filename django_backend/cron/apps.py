from django.apps import AppConfig
from django.db.models.signals import post_migrate

class MyCronConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cron'

    def ready(self):
        from .cron import start_scheduler
        start_scheduler(sender=self)
