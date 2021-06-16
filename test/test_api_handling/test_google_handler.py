import json
from unittest import TestCase

from mock import patch, MagicMock

from main.api_handling.google_handler import GoogleHandler
from main.classes.arc_solver import ArcSolver
from main.classes.decimal_location import DecimalLocation


class TestDataHandling(TestCase):
    def setUp(self) -> None:
        # For feet testing
        self.loc1 = DecimalLocation(55.111, -4.111, 30, "test")
        self.loc2 = DecimalLocation(66.111, -5.111, 30, "test2")
        self.circle = ArcSolver(3440.065, self.loc1.great_circle(self.loc2), 50)
        self.test = GoogleHandler(self.loc1, self.loc2, self.circle.y_coordinates, key="123")

        # For metres testings
        self.mloc1 = DecimalLocation(55.111, -4.111, 30, "test", height_units="METRES")
        self.mloc2 = DecimalLocation(66.111, -5.111, 30, "test2", height_units="METRES")
        self.mcircle = ArcSolver(3440.065, self.loc1.great_circle(self.loc2), 50, height="METRES")
        self.mtest = GoogleHandler(self.mloc1, self.mloc2, self.mcircle.y_coordinates, key="123", height_units="METRES")

    def test_construct_url(self):
        self.assertEqual('https://maps.googleapis.com/maps/api/elevation/json?path=55.111,-4.111|66.111,'
                         '-5.111&samples=150&key=123', self.test.request_url)

    @patch('urllib.request.urlopen')
    def test_send_request(self, mock_http_client):
        mock_http_client.return_value = "Hello"
        response = self.test.send_request()
        self.assertEqual("Hello", response)

    @patch('urllib.request.urlopen')
    def test_process_response(self, mock_http_client):
        sample_json = '''{


                            "results": [
                                {
                                    "elevation": 1,
                                    "classes": {
                                        "lat": 39.73915360,
                                        "lng": -104.98470340
                                    },
                                    "resolution": 4.771975994110107
                                },
                                {
                                    "elevation": 2,
                                    "classes": {
                                        "lat": 36.4555560,
                                        "lng": -116.8666670
                                    },
                                    "resolution": 19.08790397644043
                                }
                            ],
                            "status": "OK"
                            }'''

        mock_http_client.return_value = "Hello"
        mock_receive_request = MagicMock('main.api_handling.google_handler.GoogleHandler.receive_request')
        json_sample = json.loads(sample_json)
        # Test Feet height units
        with patch.object(GoogleHandler, 'receive_request', return_value=json_sample) as mock_method:
            a_list = self.test.process_response()
            expected_values = [3.281, 6.562]
            i = 0
            while i < len(expected_values):
                self.assertEqual(expected_values[i], a_list[i])
                i += 1

        # Test metres units
        with patch.object(GoogleHandler, 'receive_request', return_value=json_sample) as mock_method:
            a_list = self.mtest.process_response()
            expected_values = [1, 2]
            i = 0
            while i < len(expected_values):
                self.assertEqual(expected_values[i], a_list[i])
                i += 1
