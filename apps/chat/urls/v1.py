from apps.chat.views import RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
