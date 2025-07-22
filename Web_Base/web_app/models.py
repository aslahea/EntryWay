from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    # Additional fields
    phone = models.CharField(max_length=15, blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    # Soft delete flag
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        """Override default delete: perform soft delete"""
        self.is_deleted = True
        self.save()

    def __str__(self) -> str:
        return str(self.username or "")
