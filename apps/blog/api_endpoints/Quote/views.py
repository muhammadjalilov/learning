from rest_framework import viewsets

from apps.blog.api_endpoints.Quote.serializers import QuoteSerializer
from apps.blog.models import Quote


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    my_tags = ('quotes',)

__all__ = ['QuoteViewSet']