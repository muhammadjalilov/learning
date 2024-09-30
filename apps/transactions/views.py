from decimal import Decimal

from django.db.models import F, DecimalField, ExpressionWrapper
from rest_framework import generics

from apps.transactions.models import Earnings
from apps.transactions.serializers import EarningsSerializer


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
