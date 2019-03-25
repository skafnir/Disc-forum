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


class DocumentListView(generics.ListAPIView):
    """
    List all documents.
    """

    lookup_field = 'pk'
    serializer_class = DocumentSerializer

    def get_queryset(self):
        return Document.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

