from django.urls import path

from apps.newsletter.views import NewsletterCreateAPIView

urlpatterns = [
    path('v1/newsletter/',NewsletterCreateAPIView.as_view(),name='newsletter_create')
]