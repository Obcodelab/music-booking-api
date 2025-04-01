from rest_framework import permissions


class IsOrganizer(permissions.BasePermission):
    """
    Allow only event organizers to create events.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "organizer"


class IsArtist(permissions.BasePermission):
    """
    Allow only artists to create bookings.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "artist"
