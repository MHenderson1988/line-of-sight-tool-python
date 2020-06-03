from unittest import TestCase
from location import *


class TestLocation(TestCase):
    def test_longitude(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        print(location.longitude)
        location.name = "House 5"
        print(location.name)

    def test_latitude(self):
        location = Location (44.3432, +4.4543, 30, "House 2")
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