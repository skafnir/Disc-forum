from django.db.models import Q
from rest_framework import generics, mixins

from forum.models import ForumPost
from forum.permissions import IsOwnerOrReadOnly
from forum.serializers import ForumPostSerializer


class ForumPostListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    List all forum posts and create a new forum post.
    """
    lookup_field = 'pk'
    serializer_class = ForumPostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # queryset = ForumPost.objects.all()

    def get_queryset(self):
        qs = ForumPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
            # filters qs and allows to check in name and description and makes them unique
        return qs

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

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
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return ForumPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}

