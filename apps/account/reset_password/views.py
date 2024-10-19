import os

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.account.models import Account, PasswordReset
from apps.account.reset_password.serializers import ResetPasswordRequestSerializer, ResetPasswordSerializer
from dotenv import load_dotenv

from apps.account.tasks import send_email

load_dotenv()


class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        email = request.data.get('email')
        user = Account.objects.filter(email=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            reset = PasswordReset(email=email, token=token)
            reset.save()

            reset_url = f"{os.getenv('PASSWORD_RESET_BASE_URL')}/{token}"
            subject = "Password Reset"
            message = f"Your Reset link {reset_url}"
            recipient_list = [email]
            send_email.delay(subject, message, recipient_list)

            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"}, status=status.HTTP_404_NOT_FOUND)


class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        reset_obj: PasswordReset = PasswordReset.objects.filter(token=token).first()

        if not reset_obj:
            return Response({'error': 'Invalid token'}, status=400)

        user = Account.objects.filter(email=reset_obj.email).first()

        if user:
            user.set_password(request.data.get('new_password'))
            user.save()

            reset_obj.delete()
            return Response({'success': 'Password updated'})
        else:
            return Response({'error': 'No user found'}, status=404)
