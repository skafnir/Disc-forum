from rest_framework import generics, mixins


class ForumPostListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    pass


class ForumPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    pass

