import json
from unittest import TestCase
from app import create_app
from db import db
app = create_app('TEST')


class TestFilms(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()

    def test_films(self):
        resp = app.test_client().get('/films')
        actual_resp = [{"id": 1, "name": "Film Name"}]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json, actual_resp)


    def test_post_films(self):
        expected_result = [
            {'id': 1, 'name': "Joker"},
            {'id': 2, 'name': "Foker"}
        ]
        data = json.dumps({"name": "Joker"})
