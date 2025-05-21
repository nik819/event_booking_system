from django.urls import path
from authentication.controller.registration_controller import AccessTokenGenerate,ResendOtpView,RoleInformation,Registration,LoginController,ForgotPasswordController,OtpVerification

urlpatterns = [
    path('registration', Registration.as_view(), name="Registration"),
    path('login',LoginController.as_view(),name='login'),
    path('verify-otp',OtpVerification.as_view(),name='otpverification'),
    path('token/refresh',AccessTokenGenerate.as_view(),name='accesstoken'),
    path('resend',ResendOtpView.as_view(),name='resendotp'),
    path('role',RoleInformation.as_view(),name='rolenfo'),
    path('forgot-password',ForgotPasswordController.as_view(),name='forgot-password'),
]
