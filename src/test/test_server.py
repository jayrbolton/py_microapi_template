"""
Simple integration tests on the API itself.

We make actual ajax requests to the running docker container.
"""
import unittest
import requests

url = 'http://web:5000'


class TestServer(unittest.TestCase):

    def test_root(self):
        resp = requests.get(url).json()
        self.assertEqual(resp['status'], 'ok')
