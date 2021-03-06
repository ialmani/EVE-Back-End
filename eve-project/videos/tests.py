from rest_framework import status
from django.test import TestCase
from rest_framework.test import RequestsClient, APIClient
from django.contrib.auth.models import User


class VideosCreateTestCase(TestCase):
    def test_create(self):
        user = User(username='tom', password='tom')
        user.save()
        user = User.objects.get(username='tom')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.post('http://127.0.0.1:8000/videos/create', {'title': 'testcase', 'description': 'Testing the video creation.', 'video_url': 'https://youtu.be/hY7m5jjJ9mM'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class VidoesViewTestCase(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/videos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)