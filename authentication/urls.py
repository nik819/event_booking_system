from django.urls import path
from authentication.controller.registration_controller import Registration,LoginController,ForgotPasswordController,OtpVerification

urlpatterns = [
    path('registration', Registration.as_view(), name="Registration"),
    path('login',LoginController.as_view(),name='login'),
    path('verify-otp',OtpVerification.as_view(),name='otpverification'),
    path('forgot-password',ForgotPasswordController.as_view(),name='forgot-password'),
]