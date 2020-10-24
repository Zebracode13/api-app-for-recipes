from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_email(self):
        """Test of email for user creation is working propperly"""
        email = 'ze@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'ze@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if the email is valid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123') 

    def test_create_new_superuser(self):
        """test and creating super user"""
        user = get_user_model().objects.create_superuser(
            'zs@gmail.com',
            'test89'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

