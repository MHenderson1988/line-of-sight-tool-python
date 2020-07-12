from unittest import TestCase

from main.unit_conversion import metres_to_feet, nautical_miles_to_statute_miles, nautical_miles_to_kilometres, \
    nautical_miles_to_feet, nautical_miles_to_metres, earth_radius_define


class TestUnitConversion(TestCase):
    def test_metres_to_feet(self):
        self.assertEqual(3.281, metres_to_feet(1))

    def test_nautical_miles_to_metres(self):
        self.assertEqual(1852, nautical_miles_to_metres(1))

    def test_nautical_miles_to_feet(self):
        self.assertEqual(6076, nautical_miles_to_feet(1))

    def test_nautical_miles_to_statute_miles(self):
        self.assertEqual(1.151, nautical_miles_to_statute_miles(1))

    def test_nautical_miles_to_kilometres(self):
        self.assertEqual(1.852, nautical_miles_to_kilometres(1))

    def test_earth_radius_define(self):
        self.assertEqual(3440.065, earth_radius_define("Nautical miles"))