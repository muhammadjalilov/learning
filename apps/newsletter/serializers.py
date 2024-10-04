from rest_framework import serializers

from apps.newsletter.models import NewsletterEmails


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterEmails
        fields = ['email']
