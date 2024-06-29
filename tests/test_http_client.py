import unittest
from unittest.mock import patch, Mock
import sys
import os

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from helpers.httpClient import HttpClient
import config as config

class TestHttpClient(unittest.TestCase):
    def setUp(self):
        self.http_client = HttpClient(config.SERVER_URL, config.EMAIL, config.PASSWORD)

    @patch('requests.post')
    def test_login(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {'data': {'token': 'mocked_token'}}
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        self.http_client.login()
        self.assertEqual(self.http_client.token, 'mocked_token')

    @patch('requests.post')
    def test_post_data(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {'success': True}
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        data = {'test_key': 'test_value'}
        response = self.http_client.post_data('sensorReadings/12345', data)
        self.assertIsNotNone(response)
        self.assertTrue(response['success'])

    @patch('requests.get')
    def test_get_commands(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'led_value': 1}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        response = self.http_client.get_commands(config.COMMAND_ENDPOINT)
        self.assertIsNotNone(response)
        self.assertEqual(response['led_value'], 1)

if __name__ == '__main__':
    unittest.main()
