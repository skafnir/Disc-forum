from rest_framework import generics

from forum.permissions import IsOwnerOrReadOnly
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

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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


class DocumentRUView(generics.RetrieveUpdateAPIView):
    """
    Retrieve / update document.
    """

    lookup_field = 'pk'
    serializer_class = DocumentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Document.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


