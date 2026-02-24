from rest_framework import serializers
from .models import User


from .models import User, ConsultantProfile

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password", "role", "phone"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        role = validated_data.get("role")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=role,
            phone=validated_data["phone"],
        )

        # 🔥 If consultant → create ConsultantProfile
        if role == "consultant":
            ConsultantProfile.objects.create(
                user=user,
                license_number=f"LIC-{user.id}"  # temporary auto value
            )

        return user