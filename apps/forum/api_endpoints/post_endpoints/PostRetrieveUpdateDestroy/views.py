from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.forum.api_endpoints.post_endpoints.PostRetrieveUpdateDestroy.serializers import PostRetrieveSerializer
from apps.forum.models import ForumPost


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = PostRetrieveSerializer


__all__ = ['PostRetrieveUpdateDestroyView']


