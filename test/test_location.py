from unittest import TestCase

from main.location import Location


class TestLocation(TestCase):
    def test_longitude(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        print(location.longitude)
        location.name = "House 5"
        print(location.name)

    def test_latitude(self):
        location = Location(44.3432, +4.4543, 30, "House 2")
        latitude = location.latitude
        self.assertEqual(44.3432, latitude)

    def test_height(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        height = location.height
        self.assertEqual(80, height)

    def test_name(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        name = location.name
        self.assertEqual("House 1", name)

    def test_coordinates(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        self.assertEqual((55.32323, -4.37837, 80), location.coordinates_lat_long_height)

    def test_coordinates_string(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        self.assertEqual("55.32323,-4.37837", location.coordinates_lat_long_as_string)

    def test_coordinates_yx(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        self.assertEqual((-4.37837, 55.32323, 80), location.coordinates_long_lat_height)
