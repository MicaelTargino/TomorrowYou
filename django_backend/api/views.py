import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import MailMessage  # Adjust this import based on your project structure

@require_http_methods(["POST"])
def save_msg(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extracting data from the request
            subject = "Message from younger you"
            recipient_email = data.get('recipient_email')
            message_body = data.get('message_body')
            scheduled_date = data.get('scheduled_date')  # Ensure this is in 'YYYY-MM-DD' format

            # Validate the extracted data
            if not (recipient_email and message_body and scheduled_date):
                return JsonResponse({"status": 400, 'message': 'Missing required fields'})

            # Create a new MailMessage instance and save to the database
            mail_message = MailMessage(
                recipient_email=recipient_email,
                subject=subject,
                message_body=message_body,
                scheduled_date=scheduled_date
            )
            mail_message.save()

            return JsonResponse({"status": 200, 'message': 'MailMessage saved successfully'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    else:
        return JsonResponse({"status": 400, 'message': 'Method not allowed'})
