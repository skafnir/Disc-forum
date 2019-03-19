import io

from PIL import Image
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from upload.models import Document


class TestDocumentCreateView(APITestCase):
    """
    TestCase for DocumentCreateView
    """

    def generate_photo_file(self):
        """
        Generate image file
        """
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_create_item(self):
        """
        Test if we can upload a file
        """

        url = reverse('upload:document-upload')

        photo_file = self.generate_photo_file()

        data = {
            'description': 'random words',
            'document': photo_file
            }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_single_upload(self):
        """
        Test if upload generates single file
        """
        url = reverse('upload:document-upload')

        photo_file = self.generate_photo_file()

        data = {
            'description': 'random words',
            'document': photo_file
            }

        response = self.client.post(url, data, format='multipart')
        document_count = Document.objects.count()

        self.assertEqual(document_count, 1)


