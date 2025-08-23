from django.core.mail import send_mail

from core.config import EmailConfig

from celery import shared_task



@shared_task
def send_code_email(user: dict, code):
    send_mail(
        subject='!Tasdiqlash kodingiz!',
        message=f'Sizning tasdiqlash kodingiz:{code}',
        from_email=EmailConfig.EMAIL_USER,
        recipient_list=[user.get('email')],
        fail_silently=False,
    )
    return 'Success'