from django.urls import path, re_path

from upload.views import DocumentCreateView, DocumentListView

app_name = 'upload'

urlpatterns = [
    path('upload/', DocumentCreateView.as_view(), name='upload'),
    re_path(r'^upload-list/', DocumentListView.as_view(), name='upload-list'),

]