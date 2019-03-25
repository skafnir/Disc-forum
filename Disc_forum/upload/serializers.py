from rest_framework import serializers

from upload.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    """
    Serializer for Document Model
    """
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Document
        fields = [
            'pk',
            'url',
            'description',
            'document',
            'uploaded_at',
            ]

        read_only_fields = ['pk', 'url', 'uploaded_at']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)


