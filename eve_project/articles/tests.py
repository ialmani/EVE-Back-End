from rest_framework import status
from django.test import TestCase
from rest_framework.test import RequestsClient, APIClient
from django.contrib.auth.models import User


class ArticleCreateTestCase(TestCase):
    def test_create(self):
        user = User(username='tom', password='tom')
        user.save()
        user = User.objects.get(username='tom')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('http://127.0.0.1:8000/articles/create', {'title': 'testcase', 'author': 'test', 'content': 'Testing the article creation.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ArticleViewTestCase(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)