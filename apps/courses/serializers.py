from rest_framework import serializers

from apps.courses.models import Course, Category, Chapter, Topic


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = 'created_at', 'updated_at'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = 'created_at', 'updated_at'


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        exclude = 'created_at', 'updated_at'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        exclude = 'created_at', 'updated_at'
