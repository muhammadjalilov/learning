from rest_framework import serializers

from apps.forum.models import ForumPost


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = 'question', 'category', 'user'
