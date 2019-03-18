from django.urls import path

from upload.views import DocumentCreateView

app_name = 'main'

urlpatterns = [
    path('upload/', DocumentCreateView.as_view(), name='upload'),

]