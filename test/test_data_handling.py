from unittest import *

from main import data_handling


class TestDataHandling(TestCase):
    def test_construct_url(self):
        url = data_handling.construct_url('55.123,-4.123', '55.111,-4.111', '200', '123')
        self.assertEqual('https://maps.googleapis.com/maps/api/elevation/json?path=55.123,-4.123|55.111,'
                         '-4.111&samples=200&key=123', url)
