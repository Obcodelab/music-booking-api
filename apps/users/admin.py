from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ArtistProfile


class CustomUserAdmin(UserAdmin):
    list_display = ("id", "email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Role", {"fields": ("role",)}),
    )
    add_fieldsets = ((None, {"fields": ("email", "password", "role")}),)
    search_fields = ("email",)
    ordering = ("email",)


class ArtistProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


admin.site.register(User, CustomUserAdmin)
admin.site.register(ArtistProfile, ArtistProfileAdmin)
