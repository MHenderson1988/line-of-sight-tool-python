from unittest import TestCase

from main.location import Location
from main.location_reference_converter import convert_decimal_lat_long, convert_easting_northing


class TestLocationReferenceConverter(TestCase):
    def test_convert_easting_northing(self):
        list_to_test = []
        a_test_location = Location(54.906163249976245, -1.3819796963744007, 150, "Fawcett street")
        list_to_test.append(a_test_location)
        returned_list = convert_easting_northing('test_osbg36.csv')
        self.assertTrue(list_to_test.__eq__(returned_list[0]))

    def test_convert_decimal_lat_long(self):
        list_to_test = []
        a_test_location = Location(55.053203, -1.6918945, 200, "House 1")
        list_to_test.append(a_test_location)
        returned_list = convert_decimal_lat_long('test_decimal_degrees.csv')
        self.assertTrue(list_to_test.__eq__(returned_list[0]))
