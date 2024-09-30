from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenViewBase

from apps.account.login.serializers import LoginSerializer


class LoginView(TokenViewBase):
    serializer_class = LoginSerializer

__all__ = ('LoginView',)
