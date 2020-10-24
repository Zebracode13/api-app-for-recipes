from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """Test the users api public"""
    def setup(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload as successful"""
        payload = {
            'email': 'ze@gmail.com',
            'password': 'boss123',
            'name': 'boss1'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """Tests if user is creating with an existing email""""
        payload = {'email': 'zs@gmail.com', 'password': 'boss123'}
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


    def test_password_lenght(self):
        """Tests if the user password > 5 is logn enough"""

        payload = {'email': 'zele@gmail.com', 'password':'boo'}
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTT_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
