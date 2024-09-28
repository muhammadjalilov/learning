from rest_framework import serializers

from apps.courses.models import Course


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = 'created_at', 'updated_at'

