from unittest import TestCase

from main.unit_conversion import metres_to_feet, nautical_miles_to_statute_miles, nautical_miles_to_kilometres, \
    nautical_miles_to_feet, nautical_miles_to_metres, define_earth_radius, calculate_great_circle_distance, \
    miles_to_metres, miles_to_feet, kilometres_to_metres, kilometres_to_feet, convert_y_values


class TestUnitConversion(TestCase):
    def test_metres_to_feet(self):
        self.assertEqual(3.281, metres_to_feet(1))

    def test_miles_to_metres(self):
        self.assertEqual(1609.34, miles_to_metres(1))

    def test_miles_to_feet(self):
        self.assertEqual(5280, miles_to_feet(1))

    def test_kilometres_to_metres(self):
        self.assertEqual(1000, kilometres_to_metres(1))

    def test_kilmetres_to_feet(self):
        self.assertEqual(3281, kilometres_to_feet(1))

    def test_nautical_miles_to_metres(self):
        self.assertEqual(1852, nautical_miles_to_metres(1))

    def test_nautical_miles_to_feet(self):
        self.assertEqual(6076, nautical_miles_to_feet(1))

    def test_nautical_miles_to_statute_miles(self):
        self.assertEqual(1.151, nautical_miles_to_statute_miles(1))

    def test_nautical_miles_to_kilometres(self):
        self.assertEqual(1.852, nautical_miles_to_kilometres(1))

    def test_define_earth_radius(self):
        self.assertEqual(3440.065, define_earth_radius("Nautical miles"))

    def test_calculate_great_circle_distance(self):
        location_1 = [55.55, -4.00]
        location_2 = [55.00, -4.44]
        self.assertEqual(41.76108, round(calculate_great_circle_distance(location_1, location_2, "Miles"), 5))

    def test_convert_y_values(self):
        result = convert_y_values(1, "Miles", "Feet")
        self.assertEqual(5280, result)
