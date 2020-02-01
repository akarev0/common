from http import HTTPStatus

from django.test import TestCase, Client


# Create your tests here.
from django.urls import reverse


class ApiTest(TestCase):
    client = Client()

    def test_api(self):
        response = self.client.get(reverse('api_serializer', args=['key', 1]))
        self.assertTrue(response.status_code, HTTPStatus.OK)
