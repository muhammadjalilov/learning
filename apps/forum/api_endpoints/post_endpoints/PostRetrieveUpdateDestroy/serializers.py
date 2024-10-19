from rest_framework import serializers

from apps.forum.models import ForumPost


class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = 'id', 'user', 'question', 'category', 'created_at', 'updated_at'