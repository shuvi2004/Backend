from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
from .models import Notification
from django.core.mail import send_mail
from django.conf import settings

@shared_task(bind=True, max_retries=3)
def send_notification_task(self, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        
        if notification.notification_type == 'email':
            send_mail(
                'Notification',
                notification.message,
                settings.EMAIL_HOST_USER,
                [notification.user.email],
                fail_silently=False,
            )
        elif notification.notification_type == 'sms':
            # Add SMS integration logic here
            print(f"Mock SMS sent to {notification.user.username}")
        elif notification.notification_type == 'in_app':
            # Handle in-app notification logic
            pass
            
        notification.status = 'sent'
        notification.save()
        
    except Exception as e:
        notification.status = 'failed'
        notification.save()
        try:
            self.retry(exc=e, countdown=2**self.request.retries)
        except MaxRetriesExceededError:
            pass