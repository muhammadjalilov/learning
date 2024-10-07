from rest_framework import serializers, fields
from rest_framework.exceptions import ValidationError

from apps.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    password = fields.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = fields.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = ['username', 'first_name', 'last_name', 'email', 'website', 'avatar', 'is_subscribed_newsletter',
                  'password', 'confirm_password']
        extra_kwargs = {
            'password': {"write_only": True},
            'confirm_password': {"write_only": True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords should match')

        return attrs

    def validate_email(self, email):
        if email:
            if Account.objects.filter(email=email).exists():
                raise ValidationError('This email already existed')
        return email

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')
        user = Account.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
