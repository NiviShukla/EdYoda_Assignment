from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        "auth.Group", related_name="music_app_user_set", blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="music_app_user_set", blank=True
    )


class MusicFile(models.Model):
    ACCESS_TYPE_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
        ("protected", "Protected"),
    ]

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="music_files/")
    access_type = models.CharField(max_length=10, choices=ACCESS_TYPE_CHOICES)
    allowed_users = models.ManyToManyField(
        User, related_name="allowed_files", blank=True
    )

    def __str__(self):
        return self.title
