from django.utils import timezone
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.courses.models import Course
from apps.transactions.models import Earnings, CreditCard, BillingAddress, Invoice


class EarningsSerializer(serializers.ModelSerializer):
    net_revenue = serializers.SerializerMethodField()

    class Meta:
        model = Earnings
        fields = ['instructor', 'gross_revenue', 'net_revenue']

    def get_net_revenue(self, obj):
        return getattr(obj, 'net_revenue', None)


class CreditCardSerializer(serializers.ModelSerializer):
    updated = serializers.SerializerMethodField()

    class Meta:
        model = CreditCard
        exclude = ['account']

    def validate_card_number(self, card_number):
        if len(card_number) != 16:
            raise ValidationError('It should contains 16 numbers!')
        return card_number

    def validate_cvv(self, cvv):
        if len(cvv) != 3:
            raise ValidationError('It should contains 3 numbers!')
        return cvv

    def get_updated(self, obj):
        return timezone.now() - obj.updated_at


class BillingAddressSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()

    class Meta:
        model = BillingAddress
        fields = ['id', 'name', 'country', 'address', 'cards']

    def get_cards(self, obj):
        cards = obj.account.cards.all()
        return CreditCardSerializer(cards, many=True).data


class InvoiceCreateSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    class Meta:
        model = Invoice
        fields = ['billing_address', 'course', 'credit_card']
