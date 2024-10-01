from decimal import Decimal

from django.db.models import F, DecimalField, ExpressionWrapper
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from apps.transactions.models import Earnings, CreditCard, BillingAddress
from apps.transactions.serializers import EarningsSerializer, CreditCardSerializer, BillingAddressSerializer


class EarningsAPIView(generics.ListCreateAPIView):
    serializer_class = EarningsSerializer

    def get_queryset(self):
        queryset = Earnings.objects.annotate(
            net_revenue=ExpressionWrapper(
                F('gross_revenue') * Decimal('0.87'),
                output_field=DecimalField()
            )
        ).filter(instructor=self.request.user.instructor)

        return queryset


class EarningsDetailAPIView(generics.RetrieveAPIView):
    serializer_class = EarningsSerializer

    def get_queryset(self):
        queryset = Earnings.objects.annotate(
            net_revenue=ExpressionWrapper(
                F('gross_revenue') * Decimal('0.87'),
                output_field=DecimalField()
            )
        ).filter(instructor=self.request.user.instructor)

        return queryset


class CreditCardViewSet(ModelViewSet):
    serializer_class = CreditCardSerializer

    def get_queryset(self):
        return CreditCard.objects.filter(account=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class BillingAddressViewSet(ModelViewSet):
    serializer_class = BillingAddressSerializer

    def get_queryset(self):
        return BillingAddress.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
