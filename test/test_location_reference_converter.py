from unittest import TestCase

from main.location import Location
from main.location_reference_converter import convert_decimal_lat_long, convert_easting_northing, \
    convert_british_national_grid


class TestLocationReferenceConverter(TestCase):
    def test_convert_easting_northing(self):
        list_to_test = []
        a_test_location = Location(54.906163, -1.381980, 150, "Fawcett street")
        list_to_test.append(a_test_location)
        returned_list = convert_easting_northing('csv/test_osbg36.csv')
        self.assertEqual(a_test_location.latitude, returned_list[0].latitude)

    def test_convert_decimal_lat_long(self):
        list_to_test = []
        a_test_location = Location(55.053203, -1.6918945, 200, "House 1")
        list_to_test.append(a_test_location)
        returned_list = convert_decimal_lat_long('csv/test_decimal_degrees.csv')
        self.assertEqual(a_test_location.latitude, returned_list[0].latitude)

    def test_convert_british_national_grid(self):
        list_to_test = []
        a_test_location = Location(54.906163, -1.3819797, 200, "Fawcett street")
        list_to_test.append(a_test_location)
        returned_list = convert_british_national_grid('csv/test_bng.csv')
        print(returned_list[0].latitude, returned_list[0].longitude)
        self.assertEqual(round(a_test_location.latitude, 4), round(returned_list[0].latitude, 4))
