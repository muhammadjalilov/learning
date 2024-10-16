from django.urls import path, include
from rest_framework import routers

from apps.blog.api_endpoints.BlogPost import BlogPostListCreateView, BlogPostRetrieveUpdateDestroyAPIView
from apps.blog.api_endpoints.Quote import QuoteViewSet

router = routers.DefaultRouter()

router.register(r'quotes', QuoteViewSet, basename='quotes')
urlpatterns = [
    path('', include(router.urls)),
    path('blog-post', BlogPostListCreateView.as_view(), name='blog-posts'),
    path('blog-post/<pk>', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blog-post'),
]