from rest_framework import status
from django.test import TestCase
from rest_framework.test import RequestsClient, APIClient
from django.contrib.auth.models import User

def create_article():
    user = User(username='tom', password='tom')
    user.save()
    user = User.objects.get(username='tom')
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post('http://127.0.0.1:8000/articles/create', {'title': 'testcase', 'author': 'test', 'content': 'Testing the article creation.'})
    return response

class ArticleCreateTestCase(TestCase):
    def test_create_authorized(self):
        response = create_article()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_not_authorized(self):
        client = APIClient()
        response = client.post('http://127.0.0.1:8000/articles/create', {'title': 'testcase', 'author': 'test', 'content': 'Testing the article creation.'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class ArticleViewTestCase(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ArticleDetailViewTestCase(TestCase):
    def test_detail_found(self):
        client = APIClient()
        article = create_article()
        article_ID = article.json()['id']
        response = client.get('http://127.0.0.1:8000/articles/'+str(article_ID))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_not_found(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/articles/notfound')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ArticleDeleteTestCase(TestCase):
    def test_delete(self):
        client = APIClient()
        article = create_article()
        article_ID = article.json()['id']
        response = client.get('http://127.0.0.1:8000/articles/'+str(article_ID))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ArticleUpdateTestCase(TestCase):
    def test_view(self):
        client = APIClient()
        response = client.get('http://127.0.0.1:8000/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)