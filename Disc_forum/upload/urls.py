from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path

from upload.views import DocumentCreateView, DocumentListView, DocumentRUView

app_name = 'upload'

urlpatterns = [
    path('upload/', DocumentCreateView.as_view(), name='upload'),
    re_path(r'^upload-list/', DocumentListView.as_view(), name='upload-list'),
    re_path(r'^uploaded/(?P<pk>(\d)+)/$', DocumentRUView.as_view(), name='upload-ru')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

