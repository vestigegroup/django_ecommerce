from django.test import TestCase
from django.urls import reverse
from .models import Item


class ViewTests(TestCase):
    def test_home_view(self):
        url = reverse('core:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
