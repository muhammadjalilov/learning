from django.urls import include, path
from rest_framework import routers

from apps.courses import views

router = routers.DefaultRouter()
router.register('courses', views.CoursesViewSet, basename='courses'),
router.register('category', views.CategoryViewSet, basename='category'),
router.register('chapter', views.ChapterViewSet, basename='chapter'),
router.register('topic', views.TopicViewSet, basename='topic'),
app_name = 'courses'

urlpatterns = [
    path('', include(router.urls)),
]
