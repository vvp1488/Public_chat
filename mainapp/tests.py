from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Message


class MessagesTests(APITestCase):
    def test_new_message(self):

        url = reverse('new_message')
        data = {'Author': 'Гость', 'email': 'test@ukr.net', 'text': 'adasdas'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)
        self.assertEqual(Message.objects.get().email, 'test@ukr.net')