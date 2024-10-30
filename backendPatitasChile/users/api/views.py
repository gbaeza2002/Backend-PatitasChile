from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from users.api.serializer import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            # Create the user without confirmation
            user = serializer.save(is_confirmed=False)
            
            # Generar el código de verificación y su tiempo de expiración
            user.generate_verification_code()
            
            # Generate the verification code and its expiration time
            send_mail(
                subject="Codigo verificacion",
                message=f"Tu codigo de verificacion es: {user.verification_code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email]
            )
            
            return Response(
                {"detail": "Verification code sent to your email."},
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)


class VerifyCodeView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")
        
        try:
            # Search user by email
            user = User.objects.get(email=email)
            
            # Verify that the code is valid and has not expired
            if user.verification_code == code and user.verification_code_expiration > timezone.now():
                user.is_confirmed = True
                user.verification_code = None # Optional: delete code after verification
                user.verification_code_expiration = None
                user.save()
                
                return Response({"detail": "Email confirmed, registration completed."},
                                status=status.HTTP_200_OK)
            
            return Response({"detail": "Invalid or expired code."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response({"detail": "User not found."},
                            status=status.HTTP_404_NOT_FOUND)
            
class RequestPasswordResetView(APIView):
    def post(self, request):
        email = request.data.get("email")
        
        try:
            user = User.objects.get(email=email)
            user.generate_reset_code()
            
            # Send reset code via email
            send_mail(
                subject="Código de restablecimiento de contraseña",
                message=f"Tu código de restablecimiento de contraseña es: {user.reset_code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email]
            )
            
            return Response(
                {"detail": "Password reset code sent to your email."},
                status=status.HTTP_200_OK
            )
        
        except User.DoesNotExist:
            return Response(
                {"detail": "User with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND
            )
            
class VerifyResetCodeView(APIView):
    def post(self, request):
        email = request.data.get("email")
        code = request.data.get("code")
        
        try:
            user = User.objects.get(email=email)
            
            if user.reset_code == code and user.reset_code_expiration > timezone.now():
                return Response({"detail": "Code verified. You can now reset your password."},
                                status=status.HTTP_200_OK)
            
            return Response({"detail": "Invalid or expired code."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response({"detail": "User not found."},
                            status=status.HTTP_404_NOT_FOUND)

class ResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        new_password = request.data.get("new_password")
        
        try:
            user = User.objects.get(email=email)
            
            if user.reset_code_expiration > timezone.now():
                # Reset password and clear reset code
                user.password = make_password(new_password)
                user.reset_code = None
                user.reset_code_expiration = None
                user.save()
                
                return Response({"detail": "Password has been reset successfully."},
                                status=status.HTTP_200_OK)
            
            return Response({"detail": "Password reset code has expired."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        except User.DoesNotExist:
            return Response({"detail": "User not found."},
                            status=status.HTTP_404_NOT_FOUND)