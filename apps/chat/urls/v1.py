from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.chat.views import RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
