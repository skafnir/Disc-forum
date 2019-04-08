from django.conf import settings
from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Document(models.Model):
    """
    Model for uploaded documents - user, description, path to document, upload time
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username) + ' ' + self.description

    # user == owner for permission IsOwnerOrReadOnly
    @property
    def owner(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse('upload:upload-ru', kwargs={'pk': self.pk}, request=request)


