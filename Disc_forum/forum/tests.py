from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from forum.models import ForumPost

User = get_user_model()


class ForumPostListCreateAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='testUser', email='test@test.com')
        user.set_password('somerandompassword')
        user.save()
        forum_post = ForumPost.objects.create(user=user,
                                              title='Random title',
                                              content='Lorem ipsum dolor sitt amet',
                                              )

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_forum_post(self):
        service_count = ForumPost.objects.count()
        self.assertEqual(service_count, 1)
