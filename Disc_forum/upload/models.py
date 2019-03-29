from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Document(models.Model):
    """
    Model for uploaded documents - description, path to document, upload time
    """
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_api_url(self, request=None):
        return api_reverse('forum:forum-post-rud', kwargs={'pk': self.pk}, request=request)