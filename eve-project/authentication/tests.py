import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import RequestsClient, APIClient
from django.test import TestCase

def create_user():
    client = APIClient()
    data = {"username":"testcase",
            "email":"test@email.com",
            "password":"password",
            "first_name":"testFirst",
            "last_name":"testLast"}
    response = client.post("/auth/api/register", data)
    return response

class RegistrationTestCase(TestCase):
    def test_registration(self):
        response = create_user()
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LoginTestCase(TestCase):
    def test_login_user(self):
        client = APIClient()
        user = create_user()
        data = {"username": "testcase",
                "password": "password"}
        response = client.post("/api/token", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)