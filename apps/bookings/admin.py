from django.contrib import admin
from .models import Event, Booking


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "location", "organizer", "date")
    search_fields = ("title", "location")
    list_filter = ("date", "organizer")


class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "artist", "event", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("artist__email", "event__title")


admin.site.register(Event, EventAdmin)
admin.site.register(Booking, BookingAdmin)
