from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.newsletter.models import NewsletterEmails
from apps.newsletter.tasks import send_email


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterEmails
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if NewsletterEmails.objects.filter(email=email).exists():
            raise ValidationError(detail='This email already exists', code=400)

    def create(self, validated_data):
        instance = super().create(validated_data)
        send_email.delay('Congratulations',
                         'Congrats you have subscribed on our Learning Platform',
                         [instance.email]
                         )
        return instance
