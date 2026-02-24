from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import RegisterSerializer
from .profile_serializers import ConsultantProfileSerializer
from .models import User, ConsultantProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .auth_serializers import CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class ConsultantProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ConsultantProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile, created = ConsultantProfile.objects.get_or_create(user=self.request.user)
        return profile