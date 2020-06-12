from unittest import *

from main.location_reference_converter import convert_grids


class TestGridConverter(TestCase):
    def test_convert_grids(self):
        a_list = convert_grids('test_decimal_degrees.csv')
        lat = a_list[0].latitude
        long = a_list[0].longitude
        height = a_list[0].height
        name = a_list[0].name
        self.assertEqual("House 1", name)
        self.assertEqual(55.053203, lat)
        self.assertEqual(-1.6918945, long)
        self.assertEqual(200, height)
