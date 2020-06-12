from unittest import TestCase
import csv

from main.location import Location
from main.location_reference_converter import convert_decimal_lat_long


class TestLocationReferenceConverter(TestCase):
    def test_convert_grids_lat_long(self):
        list_to_test = []
        a_test_location = Location(55.053203, -1.6918945, 200, "House 1")
        list_to_test.append(a_test_location)
        returned_list = convert_decimal_lat_long('test.csv')
        self.assertTrue(list_to_test.__eq__(returned_list[0]))
