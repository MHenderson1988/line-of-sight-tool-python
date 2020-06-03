from unittest import TestCase
from location import *


class TestLocation(TestCase):
    def test_longitude(self):
        location = Location(55.32323, -4.37837, 80, "House 1")
        print(location.longitude)
        location.name = "House 5"
        print(location.name)