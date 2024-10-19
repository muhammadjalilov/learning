from datetime import datetime, timedelta

from celery import shared_task

from apps.notifications.models import PeriodNotifications
from apps.students.models import Student


@shared_task
def send_notification_for_expired_subscriptions():
    students = Student.objects.filter(period__lte=datetime.now() - timedelta(days=7))
    notifications = []
    for student in students:
        n = PeriodNotifications(
            title=f"Your subscription ends on {student.period}",
            account=student.account
        )
        notifications.append(n)
    PeriodNotifications.objects.bulk_create(notifications)
