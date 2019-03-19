from django.db import models

# Create your models here.


class Document(models.Model):
    """
    Model for uploaded documents - description, path to document, upload time
    """
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

