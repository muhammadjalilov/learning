from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.chat.views import RoomViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
