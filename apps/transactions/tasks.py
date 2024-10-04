from django.db.models import Sum

from config.celery import app
from rest_framework.generics import get_object_or_404

from apps.transactions.models import Invoice, Transactions


@app.task
def create_transaction_after_paid(invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    if invoice.paid_status and not Transactions.objects.filter(invoice=invoice).exists():
        Transactions.objects.create(
            paid_amount=invoice.amount,
            user=invoice.user,
            invoice=invoice
        )


