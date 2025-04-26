from django.urls import path
from authentication.controller.registration import Registration

urlpatterns = [
    path('registration', Registration.as_view(), name="Registration")
]