from django.db import models

from apps.courses.models import Course
from apps.shared.models import TimeStampedModel


class CreditCard(TimeStampedModel):
    card_number = models.CharField(max_length=16, unique=True)
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=3)

    class Meta:
        verbose_name = 'Credit Card'
        verbose_name_plural = 'Credit Cards'
        ordering = ['id']

    def __str__(self):
        return self.card_number


class BillingAddress(TimeStampedModel):
    country = models.CharField(max_length=30)
    address = models.TextField()
    credit_cards = models.ManyToManyField(CreditCard, related_name='billing_addresses')
    user = models.ForeignKey('apps.Account', on_delete=models.CASCADE, related_name='billing_addresses')

    class Meta:
        verbose_name = 'Billing Address'
        verbose_name_plural = 'Billing Addresses'
        ordering = ['id']

    def __str__(self):
        return self.address


class Invoice(TimeStampedModel):
    paid_status = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE, related_name='invoices')
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='invoices')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='invoices')
    user = models.ForeignKey('apps.Account', on_delete=models.CASCADE, related_name='invoices')

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['id']

    def __str__(self):
        return str(self.id)


class Transactions(TimeStampedModel):
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('apps.Account', on_delete=models.CASCADE, related_name='transactions')
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='transactions')

    class Meta:
        verbose_name = 'Transactions'
        verbose_name_plural = 'Transactions'
        ordering = ['id']

    def __str__(self):
        return str(self.id)

class Earnings(TimeStampedModel):
    instructor = models.OneToOneField('apps.Instructor', on_delete=models.CASCADE, related_name='earnings')
    gross_revenue = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Earnings'
        verbose_name_plural = 'Earnings'
        ordering = ['id']

    def __str__(self):
        return str(self.id)
