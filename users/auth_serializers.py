from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        user = self.user

        # If consultant and not verified
        if user.role == "consultant" and not user.is_verified:
            raise serializers.ValidationError(
                "Your consultant account is waiting for admin approval."
            )

        return data