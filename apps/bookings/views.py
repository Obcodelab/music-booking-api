from rest_framework import viewsets, permissions
from apps.common.permissions import IsOrganizer, IsArtist
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer


# Create your views here.
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOrganizer()]
        return [permissions.IsAuthenticated()]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsArtist()]
        return [permissions.IsAuthenticated()]
