from django.urls import path

from apps.forum.api_endpoints import post_endpoints

urlpatterns = [
    path('forum-post-categories', post_endpoints.ForumCategoryListCreateAPIView.as_view(), name='forum_categories'),
    path('forum-post/<pk>/', post_endpoints.PostRetrieveUpdateDestroyView.as_view(), name='forum_post'),
    path('forum-post', post_endpoints.ForumPostListCreateApiView.as_view(), name='forum_posts'),
]