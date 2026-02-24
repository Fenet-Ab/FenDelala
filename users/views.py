from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status
from .models import ConsultantProfile

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
class VerifyConsultantView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        try:
            profile = ConsultantProfile.objects.get(pk=pk)
        except ConsultantProfile.DoesNotExist:
            return Response({"error": "Consultant not found"}, status=404)

        profile.is_verified = True
        profile.save()

        return Response({"message": "Consultant verified successfully"})