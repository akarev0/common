from http import HTTPStatus

from django.test import TestCase, Client


# Create your tests here.
from django.urls import reverse


class MyCoreTest(TestCase):
    client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_tenant_page(self):
        response = self.client.get(reverse('tenant_list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_rooms_page(self):
        response = self.client.get(reverse('rooms-list'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_journal_page(self):
        response = self.client.get(reverse('journal_view'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_mycore(self):
        response = self.client.get(reverse('my_core_serializer', args=['tenant', '1'], kwargs={'format': 'json'}))
        self.assertTrue(response.status_code, HTTPStatus.OK)
