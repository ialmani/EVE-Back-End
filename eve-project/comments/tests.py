from rest_framework import status
from django.test import TestCase
from rest_framework.test import RequestsClient, APIClient
from django.contrib.auth.models import User
# from articles.tests import create_article


# Create your tests here.

def create_article_comment():
    user = User(username='tom', password='tom')
    user.save()
    user = User.objects.get(username='tom')
    client = APIClient()
    client.force_authenticate(user=user)
    article = client.post('http://127.0.0.1:8000/articles/create', {'title': 'testcase', 'author': 'test', 'content': 'Testing the article creation.'})
    article_ID = article.json()['id']
    response = client.post('http://127.0.0.1:8000/articles/'+str(article_ID)+'/comments/create',
                           {'article': str(article_ID), 'user': str(user.id), 'body': 'Testing the article comments.'})
    info = []
    return [response, article]

# def create_video_comment():
#     user = User(username='tom', password='tom')
#     user.save()
#     user = User.objects.get(username='tom')
#     client = APIClient()
#     client.force_authenticate(user=user)
#     video = client.post('http://127.0.0.1:8000/videos/create', {'title': 'testcase', 'description': 'test', 'video_url': 'https://www.google.com/'})
#     video_ID = video.json()['id']
#     response = client.post('http://127.0.0.1:8000/videos/'+str(video_ID)+'/comments/create',
#                            {'video': str(video_ID), 'user': str(user.id), 'body': 'Testing the video comments.'})
#     return response

class ArticleCommentCreateTestCase(TestCase):
    def test_create(self):
        response = create_article_comment()
        self.assertEqual(response[0].status_code, status.HTTP_201_CREATED)

class ArticleViewTestCase(TestCase):
    def test_view(self):
        client = APIClient()
        info = create_article_comment()
        article = info[1]
        response = client.get('http://127.0.0.1:8000/articles/'+str(article.json()['id'])+'/comments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ArticleDetailViewTestCase(TestCase):
    def test_detail(self):
        client = APIClient()
        info = create_article_comment()
        article = info[0]
        comment = info[1]
        response = client.get('http://127.0.0.1:8000/articles/'+str(article.json()['id'])+'/comments/'+str(comment.json()['id']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)