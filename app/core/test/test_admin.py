from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):
    def setup(self):
        """Test for users in application"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(email='zele@gmail.com', password='test46')
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(email='z@gmail.com', password='pass234', name='Test is my first test')
        
    def test_user_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
    
    def test_user_change_page(self):
        """test That the user edit page is properly opperating"""

        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Testes that the user page works properly"""
        url = reverse('admin:core_user_add')
        res= self.client.get(url)

        self.assertEqual(res.status_code, 200)
        