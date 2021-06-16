from unittest import TestCase

from main.classes.LocationFactory import LocationFactory
from main.classes.decimal_location import DecimalLocation


class TestLocationFactory(TestCase):
    def setUp(self) -> None:
        self.test = LocationFactory('data/test_decimal_degrees.csv')
        self.test2 = LocationFactory('data/test_osbg36.csv')

    def test_process_data(self):
        locs = self.test.locations
        for i in locs:
            self.assertIsInstance(i, DecimalLocation)

        gridlocs = self.test2.locations
        for i in gridlocs:
            self.assertIsInstance(i, DecimalLocation)
