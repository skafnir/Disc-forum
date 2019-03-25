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

        url = reverse('upload:upload')

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
        url = reverse('upload:upload')

        photo_file = self.generate_photo_file()

        data = {
            'description': 'random words',
            'document': photo_file
            }

        response = self.client.post(url, data, format='multipart')
        document_count = Document.objects.count()

        self.assertEqual(document_count, 1)

    def test_get_list(self):
        """
        Test for GET - method not allowed
        """
        data = {}
        url = reverse('upload:upload')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_put_item(self):
        """
        Test for PUT - method not allowed
        """
        data = {}
        url = reverse('upload:upload')
        response = self.client.put(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_item(self):
        """
        Test for PATCH - method not allowed
        """
        data = {}
        url = reverse('upload:upload')
        response = self.client.patch(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_item(self):
        """
        Test for DELETE - method not allowed
        """
        data = {}
        url = reverse('upload:upload')
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class TestDocumentListView(APITestCase):
    """
    TestCase for DocumentListView
    """
    def setUp(self):
        document = Document.objects.create(description='random words',
                                           document="http://127.0.0.1:8000/media/documents/"
                                                    "wccfcyberpunk20771-740x429.jpg"
                                           )

    def test_get_list(self):
        """
        Test for DocumentListView for correct response
        """
        documents = Document.objects.all()
        data = {'documents': documents}
        url = reverse('upload:upload-list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
