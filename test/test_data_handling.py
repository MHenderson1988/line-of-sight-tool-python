import json

from unittest import *
from mock import patch, Mock
from main import data_handling


class TestDataHandling(TestCase):
    def test_construct_url(self):
        url = data_handling.construct_url('55.123,-4.123', '55.111,-4.111', '200', '123')
        self.assertEqual('https://maps.googleapis.com/maps/api/elevation/json?path=55.123,-4.123|55.111,'
                         '-4.111&samples=200&key=123', url)

    @patch('urllib.request.urlopen')
    def test_send_request_google_elevation(self, mock_http_client):
        mock_http_client.return_value = "Hello"
        response = data_handling.send_request_google_elevation('https://hello.com/api/38427363')
        self.assertEqual("Hello", response)

    def test_receive_request_google_elevation(self):
        mock_response = Mock()
        mock_response.read.return_value = str.encode("{\"Number\": [1, 2, 3]}")
        json_string = data_handling.receive_request_google_elevation(mock_response)
        self.assertEqual("{\'Number\': [1, 2, 3]}", str(json_string))

    def test_process_response(self):
        sample_json = '''{


                    "results": [
                        {
                            "elevation": 1,
                            "location": {
                                "lat": 39.73915360,
                                "lng": -104.98470340
                            },
                            "resolution": 4.771975994110107
                        },
                        {
                            "elevation": 1,
                            "location": {
                                "lat": 36.4555560,
                                "lng": -116.8666670
                            },
                            "resolution": 19.08790397644043
                        }
                    ],
                    "status": "OK"
                    }'''
        sample_json_loads = json.loads(sample_json)
        expected_elevation_values = [2, 2]
        elevation_list = data_handling.process_response(sample_json_loads, [1, 1])
        self.assertListEqual(expected_elevation_values, elevation_list)
