from rest_framework import serializers

from apps.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['website', 'avatar', 'is_subscribed_newsletter', 'card']


