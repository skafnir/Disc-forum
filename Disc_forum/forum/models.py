from django.conf import settings
from django.db import models

from rest_framework.reverse import reverse as api_reverse


class ForumPost(models.Model):
    """
    Model for forum posts - user, post title, post content, timestamp
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    def get_api_url(self, request=None):
        return api_reverse('forum:forum-post-rud', kwargs={'pk': self.pk}, request=request)
