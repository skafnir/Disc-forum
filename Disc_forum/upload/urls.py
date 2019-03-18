from django.urls import path

from upload.views import DocumentCreateView

app_name = 'upload'

urlpatterns = [
    path('upload/', DocumentCreateView.as_view(), name='upload'),

]