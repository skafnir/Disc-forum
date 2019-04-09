import io

from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase

from upload.models import Document


class DocumentCreateAPITestCase(APITestCase):
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

    def setUp(self):
        """
        Set up
        """
        self.url = reverse('upload:create')
        self.username = 'john'
        self.email = 'john@snow.com'
        self.password = 'you_know_nothing'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.photo = self.generate_photo_file()

    def test_single_user(self):
        """
        Test if there is 1 user
        """
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_get_list(self):
        """
        Test for GET list - 405 method not allowed
        """
        documents = Document.objects.all()
        data = {'documents': documents}
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, 405)

    def test_create_item_with_user(self):
        """
        Test for POST document with user- 201 created
        """
        self.client.force_login(self.user)
        data = {'description': 'Random title', 'document': self.photo}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, 201)

    def test_create_item_without_user(self):
        """
        Test for POST document without user - 401 unauthorized
        """
        data = {'description': 'Random title', 'document': self.photo}
        response = self.client.post(self.url, data, format='multipart')
        self.assertEqual(response.status_code, 401)
