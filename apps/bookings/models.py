from django.db import models
from django.contrib.auth import get_user_model
from common.models import BaseModel

# Create your models here.

User = get_user_model()


class Event(BaseModel):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="organized_events",
    )

    def __str__(self):
        return f"{self.title}"


class Booking(BaseModel):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    artist = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.artist.email} for {self.event.title} - {self.status}"
