from rest_framework import serializers

from apps.blog.models import BlogPost


class BlogPostRetrieveUpdateDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
