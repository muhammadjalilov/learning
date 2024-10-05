from decimal import Decimal

from django.db.models import F, DecimalField, ExpressionWrapper, Sum
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from apps.account.permissions import IsOwnerOrReadOnly, IsOwner
from apps.courses.models import Course
from apps.transactions.models import Earnings, CreditCard, BillingAddress, Invoice
from apps.transactions.serializers import EarningsSerializer, CreditCardSerializer, BillingAddressSerializer, \
    InvoiceCreateSerializer
from config.permissions import IsStaffUserOrReadOnly, IsInstructorOrReadOnly


class EarningsAPIView(generics.ListCreateAPIView):
    serializer_class = EarningsSerializer
    permission_classes = [IsStaffUserOrReadOnly]

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
    permission_classes = [IsInstructorOrReadOnly]

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
    permission_classes = [IsOwner]

    def get_queryset(self):
        return CreditCard.objects.filter(account=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(account=self.request.user)


class BillingAddressViewSet(ModelViewSet):
    serializer_class = BillingAddressSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        return BillingAddress.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InvoiceCreateAPIView(generics.CreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceCreateSerializer
    permission_classes = [IsStaffUserOrReadOnly]

    def perform_create(self, serializer):
        course = serializer.validated_data.get('course')
        course_ids = 0
        if isinstance(course, list) and all(isinstance(course, Course) for course in course):
            course_ids = [course.id for course in course]

        total_amount = Course.objects.filter(id__in=course_ids).aggregate(Sum('price'))['price__sum'] or 0
        serializer.save(
            user=self.request.user,
            amount=total_amount
        )
