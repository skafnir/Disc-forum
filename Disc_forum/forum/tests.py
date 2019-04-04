import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse

from forum.models import ForumPost


class ForumPostListCreateAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up
        """
        self.url = reverse('forum:forum-post-create')
        self.username = 'john'
        self.email = 'john@snow.com'
        self.password = 'you_know_nothing'
        self.user = User.objects.create_user(self.username, self.email, self.password)

    def test_single_user(self):
        """
        Test if there is 1 user
        """
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_user_forum_post(self):
        """
        Test to verify user ForumPost list
        """
        ForumPost.objects.create(user=self.user, title='Random title', content='Lorem ipsum dolor sitt amet')
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == ForumPost.objects.count())

    def test_get_list(self):
        """
        Test for GET list - 200 OK
        """
        postings = ForumPost.objects.all()
        data = {'postings': postings}
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_get_item(self):
        """
        Test for GET item - 200 OK
        """
        posting = ForumPost.objects.first()
        data = {'posting': posting}
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        """
        Test for POST forum post - 201 created
        """
        self.client.force_login(self.user)
        data = {'title': 'Random title', 'content': 'Lorem ipsum dolor sitt amet'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)

    def test_put_item(self):
        """
        Test for PUT - 405 method not allowed
        """
        data = {}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 405)

    def test_patch_item(self):
        """
        Test for PATCH - 405 method not allowed
        """
        data = {}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, 405)

    def test_delete_item(self):
        """
        Test for DELETE - 405 method not allowed
        """
        data = {}
        response = self.client.delete(self.url, data)
        self.assertEqual(response.status_code, 405)



