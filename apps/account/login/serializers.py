from rest_framework.fields import CharField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    username = CharField()
    password = CharField()
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token