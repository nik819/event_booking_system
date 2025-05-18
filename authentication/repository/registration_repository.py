import logging
import os
from datetime import timedelta

from rest_framework_simplejwt.tokens import RefreshToken

from django.db.models import Q
from django.utils.timezone import now

from authentication.serilizers import RegistrationSerializers
from authentication.models import User, OTP
from authentication.utils.utils import send_otp_email_async, generate_otp
from authentication.config.config import OTP_CONFIG


class LoginRepository:
    def login_repository(emailOrUsername,password):
        # Check if user exists
        user = User.objects.filter(Q(email=emailOrUsername) | Q(username=emailOrUsername)).first()
        if not user:
            return {"error": "Invalid credentials", "status": 401}
        # Check password
        if not user.check_password(password):
            logging.warning("Login failed: Incorrect password.")
            return {"error": "Invalid credentials", "status": 401}
        # Check if user is blocked or inactive
        if user.isAdminBlock or not user.is_active:
            block_reason = "blocked by admin" if user.isAdminBlock else "deleted"
            return {"error": f"User is {block_reason}. Contact support.", "status": 403}
        if not user.allow2fa:
            response = OtpVerificationRepository.generate_tokens(user,user.allow2fa)
            return response
        if os.getenv("EVENTMANAGEMENT_LIVE") == "False":
            logging.info(f'Event Booking System={os.getenv("EVENTMANAGEMENT_LIVE")}')
            otp_code=1111
        else:
            otp_code = generate_otp()
        LoginRepository.store_otp(user,otp_code)
        send_otp_email_async(user.email, otp_code)
        return {
            "userId": str(user.id),
            "message": "OTP sent to your email. Please verify to complete login",
            "challenge": user.allow2fa
        }

    def store_otp(user, otp):
        expiry_time=now()+timedelta(seconds=OTP_CONFIG['otp_expiry'])
        OTP.objects.create(user=user.id,otp=otp,expiresAt=expiry_time)

class OtpVerificationRepository:
    def generate_tokens(user, challenge):
        refresh = RefreshToken.for_user(user)
        return {
            "challenge":challenge,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

class RegistrationRepository:
    @staticmethod
    def registration_repository(data):
        try:
            serializer = RegistrationSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return {'message': 'Registration Successful'}
            else:
                return {'error': serializer.errors}
        except Exception as e:
            return {'error': str(e)}

class ForgotPasswordRepository:
    @staticmethod
    def forgot_password_repository(email):
        try:
            user = User.objects.filter(email=email).first()
            if not user:
                return {'error': 'User not found'}
            if user.isAdminBlock or not user.is_active:
                block_reason = "blocked by admin" if user.isAdminBlock else "deleted"
                return {"error": f"User is {block_reason}. Contact support."}
            otp_code = generate_otp()
            print("----------", otp_code)
            ForgotPasswordRepository.store_otp(user, otp_code)
            send_otp_email_async(user.email, otp_code)
            return {'message': 'OTP sent to your email'}
        except Exception as e:
            return {'error': str(e)}
    
    def store_otp(user, otp):
        expiry_time=now()+timedelta(seconds=OTP_CONFIG['otp_expiry'])
        OTP.objects.create(user=user.id,otp=otp,expiresAt=expiry_time)
