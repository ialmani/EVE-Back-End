import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import RequestsClient, APIClient
from django.test import TestCase



class RegistrationTestCase(TestCase):
    def test_registration(self):
        data = {"username":"testcase", "email":"test@email.com", "password":"password", "first_name":"testFirst", "last_name":"testLast"}
        response = self.client.post("/auth/api/register", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

