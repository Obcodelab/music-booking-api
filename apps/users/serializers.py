from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ArtistProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, help_text="Hidden in response")

    class Meta:
        model = User
        fields = ["id", "email", "password", "role"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password, **validated_data)
        return user


class ArtistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistProfile
        fields = "__all__"
