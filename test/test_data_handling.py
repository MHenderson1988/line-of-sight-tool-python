from data_handling import *
from unittest import *


class TestDataHandling(TestCase):
    def test_construct_url(self):
        url = construct_url('55.123,-4.123', '55.111,-4.111', '200', '123')
        print(url)
        self.assertEqual(
            'https://maps.googleapis.com/maps/api/elevation/json?path=55.123,-4.123|55.111,-4.111&samples=200&key=123',
            url)
