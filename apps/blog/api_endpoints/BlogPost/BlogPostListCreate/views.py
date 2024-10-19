from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView

from apps.blog.api_endpoints.BlogPost.BlogPostListCreate.serializers import BlogPostListCreateSerializer
from apps.blog.models import BlogPost


class BlogPostListCreateView(ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostListCreateSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('body', 'name', 'user__username')

__all__ = ['BlogPostListCreateView']