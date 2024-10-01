from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.transactions.models import BillingAddress
from apps.transactions.views import EarningsAPIView, EarningsDetailAPIView, CreditCardViewSet, \
    BillingAddressViewSet

router = DefaultRouter()
router.register('credit-card', CreditCardViewSet, basename='creditcard')
router.register('billing-address', BillingAddressViewSet,basename='billingaddress')
urlpatterns = [
    path('earnings/', EarningsAPIView.as_view()),
    path('earnings/<int:pk>/', EarningsDetailAPIView.as_view()),
]
urlpatterns += router.urls
