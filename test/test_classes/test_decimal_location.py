import math
from unittest import TestCase

from main.classes.decimal_location import DecimalLocation


class TestLocation(TestCase):
    def setUp(self) -> None:
        # Feet
        self.test = DecimalLocation(55.111222, -4.111222, 500, "Test")
        # Metres
        self.test2 = DecimalLocation(55.111222, -4.111222, 500, "Test2", height_units="METRES")
        # For equality test
        self.test3 = DecimalLocation(66.111222, -5.111222, 20, "Test 3")

    def test_string(self):
        # Test Feet
        expected = "Test is a location of decimal latitude and longitude at latitude: 55.111222, longitude: -4.111222," \
                   "at a height of 500 FEET"
        self.assertEqual(expected, self.test.__str__())

        # Test Metres
        expected = "Test2 is a location of decimal latitude and longitude at latitude: 55.111222, longitude: -4.111222," \
                   "at a height of 500 METRES"
        self.assertEqual(expected, self.test2.__str__())

    def test_equality(self):
        self.assertTrue(self.test.__eq__(self.test2))
        self.assertFalse(self.test.__eq__(self.test3))

    def test_calculate_interval(self):
        expected_lat, expected_lon = 11.0 / 4, -1.0 / 4
        actual_lat, actual_lon = self.test.calculate_interval(self.test3, 4)
        self.assertEqual(expected_lat, actual_lat)
        self.assertEqual(expected_lon, actual_lon)

    def test_populate_path(self):
        expected = [(55.111222, -4.111222), (58.777889, -4.444555), (62.444556, -4.777888), (66.111223, -5.111221)]
        queue = self.test.populate_path(self.test3, 3)

        for i in expected:
            self.assertEqual(i, queue.popleft())

    def test_great_circle(self):
        expected = 661.0
        # Assert within 5% tolerance
        self.assertTrue(math.isclose(expected, self.test.great_circle(self.test3), rel_tol=0.05))
