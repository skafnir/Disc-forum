from rest_framework import generics, mixins

from forum.models import ForumPost
from forum.serializers import ForumPostSerializer


class ForumPostListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    List all forum posts and create a new forum post.
    """
    lookup_field = 'pk'
    serializer_class = ForumPostSerializer

    # queryset = ForumPost.objects.all()

    def get_queryset(self):
        return ForumPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ForumPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve / update / delete forum post.
    """
    lookup_field = 'pk'
    serializer_class = ForumPostSerializer

    def get_queryset(self):
        return ForumPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

