import math
from unittest import TestCase

from main.classes.decimal_location import DecimalLocation
from main.classes.LocationFactory import LocationFactory


class TestLocation(TestCase):
    def setUp(self) -> None:
        self.test = LocationFactory('../data/test_decimal_degrees.csv')
        self.test2 = LocationFactory('../data/test_osbg36.csv')

    def test_process_data(self):
        locs = self.test.process_data()
        for loc in locs:
            self.assertIsInstance(loc, DecimalLocation)

        gridlocs = self.test2.process_data()
        for loc in gridlocs:
            self.assertIsInstance(loc, DecimalLocation)
