import os
from unittest import TestCase

from main.classes.LocationFactory import LocationFactory
from main.classes.decimal_location import DecimalLocation

DECIMAL_DEGREES_FILE_NAME = "test_decimal_degrees.csv"
OSBG_FILE_NAME = "test_osbg36.csv"

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestLocationFactory(TestCase):
    def test_process_data(self):
        test = LocationFactory(self.create_test_file_path(DECIMAL_DEGREES_FILE_NAME))
        test2 = LocationFactory(self.create_test_file_path(OSBG_FILE_NAME))

        locs = test.locations
        for i in locs:
            self.assertIsInstance(i, DecimalLocation)

        gridlocs = test2.locations
        for i in gridlocs:
            self.assertIsInstance(i, DecimalLocation)

    @staticmethod
    def create_test_file_path(filename):
        return os.path.join(CURRENT_DIR, "../data/" + filename)
