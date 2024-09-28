from rest_framework import serializers

from apps.account.serializers import AccountSerializer
from apps.instructors.models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Instructor
        fields = ['account']
