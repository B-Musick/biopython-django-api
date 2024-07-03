from django.test import TestCase
from rest_framework import status
from django.urls import reverse;
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
# Reverse takes in view name and gives us the path to the rout

class GlobalTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='br', email='bmuze1@gmail.com', password='test')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()

    
