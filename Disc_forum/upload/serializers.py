from rest_framework import serializers

from upload.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for Document Model
    """

    class Meta:
        model = Document
        fields = [
            'pk',
            'description',
            'document',
            'uploaded_at',
            ]

        read_only_fields = ['pk', 'uploaded_at']



