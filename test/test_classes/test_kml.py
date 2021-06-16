from collections import deque
from unittest import TestCase

import simplekml.featgeom

from main.classes.decimal_location import DecimalLocation
from main.classes.kml import Kml


class TestKml(TestCase):
    def setUp(self) -> None:
        # Feet
        self.test = DecimalLocation(55.111222, -4.111222, 500, "Test")
        # Metres
        self.test2 = DecimalLocation(55.111222, -4.111222, 500, "Test2", height_units="METRES")
        # For equality test
        self.test3 = DecimalLocation(66.111222, -5.111222, 20, "Test 3")

        self.loc1 = deque([self.test, self.test2, self.test3])
        self.loc2 = deque([self.test3, self.test, self.test2])

        self.kml_test = Kml(self.loc1, self.loc2)

    def test_create_points(self):
        self.assertIsInstance(self.kml_test.create_points(), deque)
        points = self.kml_test.create_points()
        while points:
            self.assertIsInstance(points.pop(), simplekml.featgeom.Point)

    def test_create_linestrings(self):
        ls = self.kml_test.create_linestrings()
        while ls:
            self.assertIsInstance(ls.pop(), simplekml.featgeom.LineString)
