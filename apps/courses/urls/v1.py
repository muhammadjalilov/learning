from django.urls import include, path
from rest_framework import routers

from apps.courses import views

router = routers.DefaultRouter()
router.register('courses', views.CoursesViewSet, basename='courses')
app_name = 'courses'

urlpatterns = [
    path('', include(router.urls)),
]
