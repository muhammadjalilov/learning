from django_filters.rest_framework import DjangoFilterBackend

from apps.forum.api_endpoints.post_endpoints.PostListCreate.serializers import ForumPostSerializer
from rest_framework.generics import ListCreateAPIView

from apps.forum.models import ForumPost


class ForumPostListCreateApiView(ListCreateAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    filter_backends = (DjangoFilterBackend,)
    search_fields = ('question', 'user__username')


__all__ = ('ForumPostListCreateApiView',)