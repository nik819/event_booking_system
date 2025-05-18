from django.urls import path
from authentication.controller.registration_controller import Registration,LoginController,ForgotPasswordController

urlpatterns = [
    path('registration', Registration.as_view(), name="Registration"),
    path('login',LoginController.as_view(),name='login'),
    path('forgot-password',ForgotPasswordController.as_view(),name='forgot-password'),
]