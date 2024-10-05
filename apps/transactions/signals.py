from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.transactions.models import Invoice
from apps.transactions.tasks import create_transaction_after_paid


@receiver(post_save, sender=Invoice)
def invoice_paid_status_updated(sender, instance, **kwargs):
    if instance.paid_status:
        create_transaction_after_paid.delay(instance.id)
