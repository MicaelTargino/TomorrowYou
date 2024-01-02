import json
from datetime import datetime
from django.http import JsonResponse
from api.models import MailMessage
from .utils import get_redis_connection
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def get_emails_for_the_day():
    today = datetime.today()

    emails = MailMessage.objects.filter(scheduled_date=today, sent=False)

    # Setup Redis connection
    redis_conn = get_redis_connection()

    # Push messages to the Redis list (queue)
    for email in emails:
        email_data = {
            'recipient_email': email.recipient_email,
            'subject': email.subject,
            'message_body': email.message_body
        }
        redis_conn.rpush('email_queue', json.dumps(email_data))

    print({'status': 201, 'message': f'{emails.count()} emails queued'})

    return JsonResponse({'status': 201, 'message': f'{emails.count()} emails queued'})

def start_scheduler(sender, **kwargs):
    scheduler.add_job(get_emails_for_the_day, 'interval', minutes=1)
    scheduler.start()
    print(scheduler.get_jobs())


