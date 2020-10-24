from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setup(self):
        """Test for users in application"""
        self.client = Client()
        self.adminuser = get_user_model().objects.create_superuser(email='zele@gmail.com', password='test46')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='first_eamil@gmail.com', password='passme1234', name='Test is my first test')

    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        resp = self.client.get(url)   
        self.assertContains(resp, self.user.name)
        self.assertContains(resp, self.user.email)
    
    def test_user_change_page(self):
        """test That the user edit page is properly opperating"""

        url = reverse('admin:core_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)

    def test_create_user_page(self):
        """Testes that the user page works properly"""
        url = reverse('admin:core_user_add')
        resp= self.client.get(url)

        self.assertEqual(resp, status_code, 200)