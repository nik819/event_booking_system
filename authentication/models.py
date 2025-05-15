import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True) 
    dateOfBirth = models.DateField(null=True, blank=True)
    mobileNumber = models.CharField(null=True, max_length=15)
    password = models.CharField(null=True)

    def __str__(self):
        return self.email
    class Meta:
        db_table = "user"
