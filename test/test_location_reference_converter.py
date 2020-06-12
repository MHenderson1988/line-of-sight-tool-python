from unittest import TestCase

from main.location import Location
from main.location_reference_converter import convert_decimal_lat_long, convert_easting_northing, \
    convert_british_national_grid, conversion_type


class TestLocationReferenceConverter(TestCase):
    def test_conversion_type(self):
        decimal_lat_long_expected = [Location(55.053203, -1.6918945, 200, "House 1")]
        xy_expected = [Location(54.906163, -1.381980, 150, "Fawcett street")]
        bng_expected = [Location(51.503532, -0.12779641, 150, "10 Downing street")]

        actual_list_decimal = conversion_type('csv/test_decimal_degrees.csv', "decimal")
        actual_list_xy = conversion_type('csv/test_osbg36.csv', "xy")
        actual_bng = conversion_type('csv/test_bng.csv', "bng")
        self.assertEqual(decimal_lat_long_expected[0].latitude, actual_list_decimal[0].latitude)
        self.assertEqual(xy_expected[0].latitude, actual_list_xy[0].latitude)
        self.assertEqual(round(bng_expected[0].latitude, 4), round(actual_bng[0].latitude, 4))

    def test_convert_easting_northing(self):
        list_to_test = [Location(54.906163, -1.381980, 150, "Fawcett street")]
        returned_list = convert_easting_northing('csv/test_osbg36.csv')
        self.assertEqual(list_to_test[0].latitude, returned_list[0].latitude)

    def test_convert_decimal_lat_long(self):
        list_to_test = [Location(55.053203, -1.6918945, 200, "House 1")]
        returned_list = convert_decimal_lat_long('csv/test_decimal_degrees.csv')
        self.assertEqual(list_to_test[0].latitude, returned_list[0].latitude)

    def test_convert_british_national_grid(self):
        list_to_test = [Location(51.503532, -0.12779641, 200, "10 Downing street")]
        returned_list = convert_british_national_grid('csv/test_bng.csv')
        self.assertEqual(round(list_to_test[0].latitude, 4), round(returned_list[0].latitude, 4))
