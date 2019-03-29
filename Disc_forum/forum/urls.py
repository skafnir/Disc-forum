from django.urls import path, re_path

from forum.views import ForumPostListCreateView, ForumPostRUDView

app_name = 'forum'

urlpatterns = [
    path('post-list-create/', ForumPostListCreateView.as_view(), name='forum-post-create'),
    re_path(r'^post-rud/(?P<pk>(\d)+)/$', ForumPostRUDView.as_view(), name='forum-post-rud'),

]

