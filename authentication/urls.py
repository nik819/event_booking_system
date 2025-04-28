from django.urls import path
from authentication.controller.registration_controller import Registration,LoginController

urlpatterns = [
    path('registration', Registration.as_view(), name="Registration"),
    path('login',LoginController.as_view(),name='login')
]