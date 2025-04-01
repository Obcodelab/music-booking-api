from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from .models import ArtistProfile
from .serializers import UserSerializer, ArtistProfileSerializer

User = get_user_model()
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class ArtistProfileViewSet(viewsets.ModelViewSet):
    queryset = ArtistProfile.objects.all()
    serializer_class = ArtistProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
