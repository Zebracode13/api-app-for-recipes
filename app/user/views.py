from rest_framework import generics
from user.serializers import UserSerializer
# Create your views here.

class UserViewCreate(generics.ListCreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer