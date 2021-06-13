from unittest import TestCase

from main.classes.grid_location import GridLocation


class TestLocation(TestCase):
    def setUp(self) -> None:
        # Feet
        self.test = GridLocation(568421, 140555, 500, "Test")
        # Metres
        self.test2 = GridLocation(568421, 140555, 500, "Test2", height_units="METRES")

    def test_string(self):
        # Test Feet
        expected = "Test is a location of easting and northing grid coordinates at northing: 568421, easting: 140555," \
                   " at a height of 500 FEET"
        self.assertEqual(expected, self.test.__str__())

        # Test Metres
        expected = "Test2 is a location of easting and northing grid coordinates at northing: 568421, easting: 140555," \
                   " at a height of 500 METRES"
        self.assertEqual(expected, self.test2.__str__())
