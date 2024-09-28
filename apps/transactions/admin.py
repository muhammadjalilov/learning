from django.contrib import admin

from apps.transactions.models import CreditCard, BillingAddress, Invoice, Transactions, Earnings


@admin.register(CreditCard)
class CreditCardAdmin(admin.ModelAdmin):
    list_display = ['card_number', 'expired_date', 'cvv']


@admin.register(BillingAddress)
class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['country', 'address']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['paid_status', 'amount']


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ['paid_amount', 'user']


@admin.register(Earnings)
class EarningsAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'gross_revenue']
