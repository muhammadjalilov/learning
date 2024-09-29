from rest_framework import serializers

from apps.account.serializers import AccountSerializer
from apps.students.models import Student


class StudentSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Student
        fields = ['id','account', 'subscription_type']


    def create(self, validated_data):
        account_data = validated_data.pop('account', None)

        account_serializer = AccountSerializer(data=account_data)
        account_serializer.is_valid(raise_exception=True)
        account = account_serializer.save()
        account.save()

        student = Student.objects.create(account=account)
        student.save()

        return student

    def update(self, instance, validated_data):
        account_data = validated_data.pop('account', None)
        instance = super().update(instance, validated_data)

        if account_data:
            account = instance.account
            account_serializer = AccountSerializer(account, data=account_data, partial=True)
            account_serializer.is_valid(raise_exception=True)
            account_serializer.save()
            if account_data.get('password'):
                account.set_password('password')
                account.save()

            return instance
