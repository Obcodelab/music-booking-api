from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.common.models import BaseModel
from .managers import CustomUserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    ROLE_CHOICES = [
        ("artist", "Artist"),
        ("organizer", "Organizer"),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class ArtistProfile(BaseModel):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="artist_profile"
    )
    bio = models.TextField()
    genre = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"
