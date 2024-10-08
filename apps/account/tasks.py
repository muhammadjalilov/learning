import os

from celery import shared_task
from django.core.mail import send_mail

from apps.account.models import Account, EmailNotification
from config.celery import app


@shared_task
def email_request_notification():
    users = Account.objects.filter(email='')
    notes = []
    if not EmailNotification.objects.filter(account__in=users):
        for user in users:
            note = EmailNotification(account=user,
                              notification="Please fill in your email for account recovery and other sessions."
                              )
            notes.append(note)
        if notes:
            EmailNotification.objects.bulk_create(notes)


@shared_task
def delete_notifications_for_filled_emails():
    users = Account.objects.filter(email__isnull=False).exclude(email='')
    EmailNotification.objects.filter(account__in=users).delete()

@app.task
def send_email(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=recipient_list
    )



