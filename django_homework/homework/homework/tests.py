from http import HTTPStatus

import requests
from django.test import TestCase
from django.test import Client
from django.urls import reverse
from .settings import POKEMON_URL


class StatusViewTests(TestCase):
    client = Client()

    def test_for_all_URL(self):
        testing_url = ('health_check', 'index', 'question')
        for url in testing_url:
            with self.subTest(url=url):
                response = self.client.get(reverse(url))
                assert response.status_code == HTTPStatus.OK
        response = requests.get(f'{POKEMON_URL}')
        assert response.status_code == HTTPStatus.OK


class DataTests(TestCase):

    def test_data_is_not_None(self):
        response = requests.get(f'{POKEMON_URL}/type/3')
        data = [f"{p['pokemon']['name']}" for p in response.json()['pokemon']]
        pokemon = 'pikachu'
        self.assertIsNotNone(data)
        self.assertNotIn(pokemon, data)
