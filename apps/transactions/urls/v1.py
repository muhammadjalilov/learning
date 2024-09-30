from django.urls import path

from apps.transactions.views import EarningsAPIView, EarningsDetailAPIView

urlpatterns = [
    path('earnings/', EarningsAPIView.as_view()),
    path('earnings/<int:pk>/', EarningsDetailAPIView.as_view()),
]
