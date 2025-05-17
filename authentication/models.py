import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.timezone import now

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dateOfBirth = models.DateField(null=True, blank=True)
    mobileNo = models.CharField(max_length=15, blank=True, null=True)
    profileImage = models.ImageField(
        upload_to="user_images/",
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        blank=True,
        null=True
    )
    allow2fa=models.BooleanField(default=False)
    isAdminBlock=models.BooleanField(default=False)

    def _str_(self):
        return self.email
    class Meta:
        db_table = "user"

class OTP(models.Model):
    otpId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=40)
    otp = models.CharField(max_length=6)
    createdAt = models.DateTimeField(auto_now_add=True)
    expiresAt = models.DateTimeField()
    isVerified = models.BooleanField(default=False)
    attemptCount = models.PositiveIntegerField(default=0)

    def is_expired(self):
        return now() > self.expiresAt

    def increment_attempts(self):
        self.attemptCount += 1
        self.save()

    class Meta:
        db_table = "otp"