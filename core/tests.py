from django.test import TestCase
from django.urls import reverse
from .forms import PaymentForm


class ViewTests(TestCase):
    def test_home_view(self):
        url = reverse('core:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class FormTests(TestCase):
    def test_valid_form(self):
        data = {'stripeToken': 'test-token', 'save': True, 'use_default': False}
        form = PaymentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'stripeToken': 12, 'save': True, 'use_default': 'False'}
        form = PaymentForm(data=data)
        self.assertTrue(form.is_valid())
