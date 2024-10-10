from rest_framework import serializers

from apps.forum.models import ForumCategory


class ForumCategoriesListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumCategory
        fields = 'id', 'name', 'created_at', 'is_verified'