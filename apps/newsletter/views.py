from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.newsletter.models import NewsletterEmails
from apps.newsletter.serializers import NewsletterSerializer
from apps.newsletter.utils import get_client_ip


class NewsletterCreateAPIView(generics.CreateAPIView):
    queryset = NewsletterEmails.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        remote_address = get_client_ip(self.request)
        serializer.save(remote_address=remote_address)
