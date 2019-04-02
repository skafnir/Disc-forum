from django.contrib.auth import get_user_model
from rest_framework import status, request
from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse as api_reverse

from forum.models import ForumPost


User = get_user_model()


class ForumPostListCreateAPITestCase(APITestCase):
    def setUp(self):
        """
        Set up - creating user and forums post
        """
        user = User(username='testUser', email='test@test.com')
        user.set_password('somerandompassword')
        user.save()
        forum_post = ForumPost.objects.create(user=user,
                                              title='Random title',
                                              content='Lorem ipsum dolor sitt amet',
                                              )

    def test_single_user(self):
        """
        Test if there is 1 user
        """
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_forum_post(self):
        """
        Test if there is 1 forum post
        """
        forum_post_count = ForumPost.objects.count()
        self.assertEqual(forum_post_count, 1)

    def test_get_list(self):
        """
        Test for GET list - 200 OK
        """
        postings = ForumPost.objects.all()
        url = api_reverse('forum:forum-post-create')
        data = {'postings': postings}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_item(self):
        """
        Test for GET item - 200 OK
        """
        posting = ForumPost.objects.first()
        url = api_reverse('forum:forum-post-create')
        data = {'posting': posting}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item(self):    # TODO - ValueError: Cannot assign "<django.contrib.auth.models.AnonymousUser object
        """
        Test for POST - 200 OK
        """
        # user = User.objects.get(username='testUser')
        url = api_reverse('forum:forum-post-create')
        data = {'title': 'Some title', 'content': 'Some content'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)





