from django.urls import path, include
from rest_framework import routers

from apps.blog.api_endpoints.BlogPost import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyAPIView
from apps.blog.api_endpoints.Quote import QuoteViewSet

router = routers.DefaultRouter()

router.register('quotes', QuoteViewSet, basename='quotes')

urlpatterns = [
    path('blog-post', BlogPostListCreateView.as_view(), name='blog-posts'),
    path('blog-post/<pk>', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blog-post'),
    path('', include(router.urls)),
]
