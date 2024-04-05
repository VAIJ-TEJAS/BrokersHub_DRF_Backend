from django.core.mail import send_mail
from django.utils.timezone import now, timedelta
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from user.models import User
from user.serializers import UserSerializer
from utils.email_dynamic_sender import send_email_with_dynamic_sender
from .models import OTP
import random


class GenerateOTPRegister(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if a user with the given email already exists
        if User.objects.filter(email=email).exists():
            # Return an error response if user already exists
            return Response(
                {"error": "User with this email already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Generate a 6-digit OTP
        otp_code = "".join([str(random.randint(0, 9)) for _ in range(6)])

        # Set OTP expiration time (e.g., 10 minutes from now)
        expires_at = now() + timedelta(minutes=10)

        # Create OTP object
        OTP.objects.create(email=email, code=otp_code, expires_at=expires_at)

        # Send OTP via email
        send_email_with_dynamic_sender(
            subject="Your OTP",
            message=f"Your OTP is {otp_code}. It will expire in 10 minutes.",
            from_email="verification@thebrokershub.in",
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({"message": "OTP sent to email."}, status=status.HTTP_200_OK)


class GenerateOTPResetPassword(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if not email:
            return Response(
                {"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        # Check if a user with the given email exists
        if not User.objects.filter(email=email).exists():
            # Return an error response if no user is found
            return Response(
                {"error": "No user found with this email"},
                status=status.HTTP_404_NOT_FOUND
            )

        # Generate a 6-digit OTP
        otp_code = "".join([str(random.randint(0, 9)) for _ in range(6)])

        # Set OTP expiration time (e.g., 10 minutes from now)
        expires_at = now() + timedelta(minutes=10)

        # Create OTP object
        OTP.objects.create(email=email, code=otp_code, expires_at=expires_at)

        # Send OTP via email
        send_email_with_dynamic_sender(
            subject="Your OTP",
            message=f"Your OTP is {otp_code}. It will expire in 10 minutes.",
            from_email="verification@thebrokershub.in",
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({"message": "OTP sent to email."}, status=status.HTTP_200_OK)


class VerifyOTP(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        otp_code = request.data.get("otp")
        user_data = request.data.get("user_data")

        if not email or not otp_code or not user_data:
            return Response(
                {"error": "Email, OTP, and user data are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Attempt to retrieve the relevant OTP object
        try:
            otp_obj = OTP.objects.get(email=email, code=otp_code, is_used=False)
        except OTP.DoesNotExist:
            return Response(
                {"error": "Invalid OTP or email"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the OTP is expired
        if otp_obj.expires_at < now():
            return Response(
                {"error": "OTP has expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        # Mark OTP as used (to prevent reuse)
        otp_obj.is_used = True
        otp_obj.save()

        # Here, create the user since OTP is valid
        # Assuming user_data is a dict that User model can accept
        user_data["email"] = email  # Ensure email is included in user_data
        if "password" in user_data:
            user_data["password"] = make_password(user_data["password"])

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            token = Token.objects.create(user=user)
            return Response(
                {"token": token.key, "user": user_serializer.data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPassword(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        otp_code = request.data.get("otp")
        new_password = request.data.get("new_password")

        if not all([email, otp_code, new_password]):
            return Response(
                {"error": "Email, OTP, and new password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Validate OTP
        try:
            otp_obj = OTP.objects.get(email=email, code=otp_code, expires_at__gt=now())
        except OTP.DoesNotExist:
            return Response(
                {"error": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST
            )

        # Update user's password
        user = User.objects.get(email=email)
        user.password = make_password(new_password)
        user.save()

        # Optionally, delete the OTP after use
        otp_obj.delete()

        return Response(
            {"message": "Password reset successfully."}, status=status.HTTP_200_OK
        )
