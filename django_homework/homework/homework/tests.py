from http import HTTPStatus

import requests
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .settings import POKEMON_URL


class StatusViewTests(TestCase):
    client = Client()

    def test_status_view(self):
        response = self.client.get(reverse('health_check'))
        assert response.status_code == HTTPStatus.OK

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == HTTPStatus.OK

    def test_question_view(self):
        response = self.client.get(reverse('question'))
        assert response.status_code == HTTPStatus.OK


class DataTests(TestCase):

    def test_pokemon_API_response(self):
        response = requests.get(f'{POKEMON_URL}/type/3')
        assert response.status_code == HTTPStatus.OK

    def test_data_is_not_None(self):
        response = requests.get(f'{POKEMON_URL}/type/3')
        data = [f"{p['pokemon']['name']}" for p in response.json()['pokemon']]
        self.assertIsNotNone(data)
