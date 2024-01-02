from django.db import models
from django.utils import timezone

class MailMessage(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    message_body = models.TextField()
    scheduled_date = models.DateField()
    sent = models.BooleanField(default=False)