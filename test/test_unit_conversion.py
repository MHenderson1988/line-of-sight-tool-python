from unittest import TestCase

from main.unit_conversion import metres_to_feet, nautical_miles_to_statute_miles, nautical_miles_to_kilometres


class test_unit_conversion(TestCase):
    def test_value_to_convert(self):
        self.assertEqual(3.28084, metres_to_feet(1))

    def test_nautical_miles_to_statute_miles(self):
        self.assertEqual(1.151, nautical_miles_to_statute_miles(1))

    def test_nautical_miles_to_kilometres(self):
        self.assertEqual(1.852, nautical_miles_to_kilometres(1))
