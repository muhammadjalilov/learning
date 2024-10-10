from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from apps.forum.api_endpoints.post_endpoints.PostCategories.serializers import ForumCategoriesListCreateSerializer
from apps.forum.models import ForumCategory


class ForumCategoryListCreateAPIView(ListCreateAPIView):
    queryset = ForumCategory.objects.all()
    serializer_class = ForumCategoriesListCreateSerializer


__all__ = ('ForumCategoryListCreateAPIView',)



