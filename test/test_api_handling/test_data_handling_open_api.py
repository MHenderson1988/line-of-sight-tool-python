from unittest import TestCase

from mock import patch

from main.api_handling.data_handling_open_api import construct_json_post_data, construct_url_open_elevation, \
    send_json_data_to_open_api
from main.classes import Location


class TestDataHandlingOpenApi(TestCase):
    def test_construct_url_open_elevation(self):
        expected_url = "https://api.open-elevation.com/api/v1/lookup \\"
        actual_url = construct_url_open_elevation()
        self.assertEqual(expected_url, actual_url)

    def test_construct_json_post_data(self):
        location_one = Location(55.55, -4.44, 150, "Position 1")
        location_two = Location(55.44, -4.33, 120, "Position 2")
        return construct_json_post_data(location_one, location_two, 2)

    @patch('requests.post')
    def test_send_json_data_to_open_api(self, mock_http_client):
        mock_http_client.return_value = "Hello"
        location_one = Location(55.55, -4.44, 150, "Position 1")
        location_two = Location(55.44, -4.33, 120, "Position 2")
        mock_response = send_json_data_to_open_api(location_one, location_two, 3)
        self.assertEqual("Hello", mock_response)
