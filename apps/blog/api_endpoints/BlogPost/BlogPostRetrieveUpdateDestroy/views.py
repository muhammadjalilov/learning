from rest_framework import generics

from apps.blog.api_endpoints.BlogPost.BlogPostRetrieveUpdateDestroy.serializers import \
    BlogPostRetrieveUpdateDestroySerializer
from apps.blog.models import BlogPost


class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostRetrieveUpdateDestroySerializer

__all__ = ['BlogPostRetrieveUpdateDestroyAPIView']