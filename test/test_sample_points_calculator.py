from unittest import TestCase

from main.location import Location
from main.sample_points_calculator import calculate_intervals


class TestSamplePointsCalculator(TestCase):
    def test_calculate_intervals(self):
        location_one = Location(54.906163, -1.381980, 150, "Fawcett street")
        location_two = Location(51.503532, -0.127796, 150, "10 Downing street")

        expected_latitude = -3.402631
        expected_longitude = 1.254184
        actual_latitude, actual_longitude = calculate_intervals(location_one, location_two)
        self.assertEqual((expected_latitude, expected_longitude), (round(actual_latitude, 6), actual_longitude))
