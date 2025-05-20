from django.contrib import admin
from authentication.models import User,OTP

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")

# Register your models here.
@admin.register(OTP)
class OTP(admin.ModelAdmin):
    list_display = ("otpId", "user", "otp","createdAt", "expiresAt", "isVerified", "attemptCount")