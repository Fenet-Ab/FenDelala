from rest_framework import serializers
from .models import ConsultantProfile
from .utils import upload_document_to_supabase

class ConsultantProfileSerializer(serializers.ModelSerializer):
    document = serializers.FileField(write_only=True, required=True)

    class Meta:
        model = ConsultantProfile
        fields = ['license_number', 'document', 'is_verified']
        read_only_fields = ['is_verified']

    def update(self, instance, validated_data):
        document = validated_data.pop('document', None)
        if document:
            # Upload to Supabase
            filename = f"documents/{instance.user.username}_{document.name}"
            public_url = upload_document_to_supabase(document, filename)
            instance.document = public_url

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance