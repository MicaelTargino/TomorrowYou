from django.urls import path
from . import cron 


urlpatterns = [
    path('', cron.get_emails_for_the_day)
]
