from rest_framework import serializers

from forum.models import ForumPost


class ForumPostSerializer(serializers.ModelSerializer):
    """
    Serializer for ForumPost Model
    """
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ForumPost
        fields = [
            'pk',
            'url',
            'user',
            'title',
            'content',
            'timestamp',
            ]

        read_only_fields = ['pk', 'url', 'user', 'timestamp']

    def get_url(self, obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)

    def validate_title_unique(self, value):
        qs = ForumPost.objects.filter(name_iexact=value)
        if self.instance:                                   # excluding instance
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Title already been used")
        return value

