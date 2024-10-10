from rest_framework import serializers

from apps.blog.models import BlogPost


class BlogPostListCreateSerializer(serializers.Serializer):
    class Meta:
        model = BlogPost
        fields = 'id', 'name', 'created_at', 'updated_at', 'body', 'account', 'quote'
