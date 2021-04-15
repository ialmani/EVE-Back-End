# from api.settings import AUTH_USER_MODEL
from rest_framework import status
from django.test import TestCase
from rest_framework.test import RequestsClient, APIClient
from django.contrib.auth.models import User


def create_video():
    user = User(username='tom', password='tom')
    user.save()
    user = User.objects.get(username='tom')
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post('http://127.0.0.1:8000/videos/create', {'title': 'testcase', 'user_id': '1','description': 'test', 'video_url': 'https://www.google.com/'})
    return response

class VideoCreateTestCase(TestCase):
    def test_create(self):
        response = create_video()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_not_authorized(self):
        client = APIClient()
        response = client.post('http://127.0.0.1:8000/videos/create', {'title': 'testcase', 'description': 'test', 'video_url': 'https://www.google.com/'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class VideoViewTestCase(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/videos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ArticleDetailViewTestCase(TestCase):
    def test_detail(self):
        client = APIClient()
        video = create_video()
        video_ID = video.json()['id']
        response = client.get('http://127.0.0.1:8000/videos/'+str(video_ID))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_not_found(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/videos/notfound')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
