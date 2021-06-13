from unittest import TestCase

from main.classes.grid_location import GridLocation


class TestLocation(TestCase):
    def setUp(self) -> None:
        # Feet
        self.test = GridLocation(568421, 140555, 500, "Test")
        # Metres
        self.test2 = GridLocation(568421, 140555, 500, "Test2", height_units="METRES")
        # For equality test
        self.test3 = GridLocation(568421, 240555, 200, "Test")

    def test_string(self):
        # Test Feet
        expected = "Test is a location of easting and northing grid coordinates at northing: 568421, easting: 140555," \
                   " at a height of 500 FEET"
        self.assertEqual(expected, self.test.__str__())

        # Test Metres
        expected = "Test2 is a location of easting and northing grid coordinates at northing: 568421, easting: 140555," \
                   " at a height of 500 METRES"
        self.assertEqual(expected, self.test2.__str__())

    def test_equality(self):
        self.assertTrue(self.test.__eq__(self.test2))
        self.assertFalse(self.test.__eq__(self.test3))

    def test_to_decimal(self):
        # Tested using - https://webapps.bgs.ac.uk/data/webservices/convertForm.cfm#bngToLatLng
        newDecimal = self.test.to_decimal()
        self.assertTrue(54.942772, newDecimal.y)
        self.assertTrue(-6.052620, newDecimal.x)
