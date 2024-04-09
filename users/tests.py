from django.contrib.auth.models import Group
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.profile_url = reverse('view_profile')
        self.edit_profile_url = reverse('edit_profile')
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.group = Group.objects.create(name='Leasers')

    def test_profile_GET(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/view_profile.html')

    def test_edit_profile_POST(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(self.edit_profile_url, {
            'username': 'testuser',
            'user_type': 'leaser',
            'age': 30
        })

        self.assertEquals(response.status_code, 302)
