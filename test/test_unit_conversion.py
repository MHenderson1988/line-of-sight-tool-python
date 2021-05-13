from unittest import TestCase

from main.unit_conversion import metres_to_feet, define_earth_radius, calculate_great_circle_distance, convert_y_values


class TestUnitConversion(TestCase):
    def test_metres_to_feet(self):
        self.assertEqual(3.281, metres_to_feet(1))

    def test_define_earth_radius(self):
        self.assertEqual(3440.065, define_earth_radius("Nautical miles"))

    def test_calculate_great_circle_distance(self):
        location_1 = [55.55, -4.00]
        location_2 = [55.00, -4.44]
        self.assertEqual(41.76108, round(calculate_great_circle_distance(location_1, location_2, "Miles"), 5))

    def test_convert_y_values(self):
        result = convert_y_values(1, "Miles", "Feet")
        self.assertEqual(5280, result)
