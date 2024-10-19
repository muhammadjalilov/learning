from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from apps.account import login, reset_password

urlpatterns = [
    path('login/', login.LoginView.as_view(), ),
    path('reset-password-request/', reset_password.RequestPasswordReset.as_view(), name='request_password_reset'),
    path('reset-password/<str:token>/', reset_password.ResetPassword.as_view(), name='reset-password'),
    # path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    # path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
]
