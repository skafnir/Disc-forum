import json

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse

from forum.models import ForumPost
from forum.serializers import ForumPostSerializer


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

    def test_create_item_with_user(self):
        """
        Test for POST forum post - 201 created
        """
        self.client.force_login(self.user)
        data = {'title': 'Random title', 'content': 'Lorem ipsum dolor sitt amet'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)

    def test_create_item_without_user(self):
        """
        Test for POST forum post - 401 unauthorized
        """
        data = {'title': 'Random title', 'content': 'Lorem ipsum dolor sitt amet'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 401)

    def test_put_item(self):
        """
        Test for PUT - 405 method not allowed
        """
        self.client.force_login(self.user)
        data = {}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 405)

    def test_patch_item(self):
        """
        Test for PATCH - 405 method not allowed
        """
        self.client.force_login(self.user)
        data = {}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, 405)

    def test_delete_item(self):
        """
        Test for DELETE - 405 method not allowed
        """
        self.client.force_login(self.user)
        data = {}
        response = self.client.delete(self.url, data)
        self.assertEqual(response.status_code, 405)


class ForumPostRUDAPITestCase(APITestCase):

    def setUp(self):
        """
        Set up
        """
        self.username = 'john'
        self.email = 'john@snow.com'
        self.password = 'you_know_nothing'
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.forum_post = ForumPost.objects.create(user=self.user,
                                                   title='Random title',
                                                   content='Lorem ipsum dolor sitt amet',
                                                   )
        self.url = reverse('forum:forum-post-rud', kwargs={'pk': self.forum_post.pk})

    def test_single_user(self):
        """
        Test if there is 1 user
        """
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_get_item_correct_user(self):
        """
        Test for GET item - correct user - 200 OK
        """
        posting = ForumPost.objects.first()
        data = {'posting': posting}
        response = self.client.get(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_create_item_correct_user(self):
        """
        Test for POST - correct user - 405 method not allowed
        """
        self.client.force_login(self.user)
        data = {'title': 'Random title', 'content': 'Lorem ipsum dolor sitt amet'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 405)

    def test_put_item_correct_user(self):
        """
        Test for PUT - correct user - 200 OK
        """
        self.client.force_login(self.user)
        data = {'title': 'New title'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        forum_post = ForumPost.objects.get(id=self.forum_post.id)
        self.assertEqual(response_data.get("title"), forum_post.title)

    def test_patch_item_correct_user(self):
        """
        Test for PATCH - correct user - 200 OK
        """
        self.client.force_login(self.user)
        data = {'title': 'Another new title'}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        forum_post = ForumPost.objects.get(id=self.forum_post.id)
        self.assertEqual(response_data.get("title"), forum_post.title)

    def test_delete_item_correct_user(self):
        """
        Test for DELETE - correct user - 204 no content
        """
        self.client.force_login(self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)

    def test_put_item_incorrect_user(self):
        """
        Test for PUT - incorrect user - 403 forbidden
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        self.client.force_login(new_user)
        data = {'title': 'New title'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_patch_item_incorrect_user(self):
        """
        Test for PATCH - incorrect user - 403 forbidden
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        self.client.force_login(new_user)
        data = {'title': 'Another new title'}
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, 403)

    def test_delete_item_incorrect_user(self):
        """
        Test for DELETE - incorrect user - 403 forbidden
        """
        new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
        self.client.force_login(new_user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 403)


