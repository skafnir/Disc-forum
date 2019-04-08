from django.contrib.auth.models import User
from rest_framework import serializers

from upload.models import Document


class DocumentUserSerializer(serializers.ModelSerializer):
    """
    Serializer for Document User
    """
    class Meta:
        model = User
        fields = ("id", "username", "email")


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for Document Model
    """
    user = DocumentUserSerializer(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Document
        fields = [
            'pk',
            'url',
            'user',
            'description',
            'document',
            'timestamp',
            ]

        read_only_fields = ['pk', 'user', 'url', 'timestamp']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

