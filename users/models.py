from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('consultant', 'Consultant'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.role}"

from django.conf import settings

class ConsultantProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name="consultant_profile"
    )
    license_number = models.CharField(max_length=100, unique=True)
    document = models.TextField(blank=True, null=True)  # store Supabase file URL here
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Consultant Profile"