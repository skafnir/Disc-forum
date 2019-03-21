from rest_framework import generics

from upload.models import Document
from upload.serializers import DocumentSerializer


class DocumentCreateView(generics.CreateAPIView):
    """
    Create a new document.
    """

    lookup_field = 'pk'
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.all()



