from unittest import TestCase

from main.classes.decimal_location import DecimalLocation


class TestLocation(TestCase):
    def setUp(self) -> None:
        # Feet
        self.test = DecimalLocation(55.11, -4.11, 500, "Test")
        # Metres
        self.test2 = DecimalLocation(55.11, -4.11, 500, "Test2", height_units="METRES")
        # For equality test
        self.test3 = DecimalLocation(66.11, -5.11, 20, "Test 3")

    def test_string(self):
        # Test Feet
        expected = "Test is a location of decimal latitude and longitude at latitude: 55.11, longitude: -4.11," \
                   "at a height of 500 FEET"
        self.assertEqual(expected, self.test.__str__())

        # Test Metres
        expected = "Test2 is a location of decimal latitude and longitude at latitude: 55.11, longitude: -4.11," \
                   "at a height of 500 METRES"
        self.assertEqual(expected, self.test2.__str__())

    def test_equality(self):
        self.assertTrue(self.test.__eq__(self.test2))
        self.assertFalse(self.test.__eq__(self.test3))

    def test_populate_path(self):
        self.test.populate_path(self.test3, 20)
