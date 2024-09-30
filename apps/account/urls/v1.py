from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from apps.account import login

urlpatterns = [
    path('login/', login.LoginView.as_view(), )
    # path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    # path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
]
