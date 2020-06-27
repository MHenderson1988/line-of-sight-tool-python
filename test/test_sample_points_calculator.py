from unittest import TestCase

from main.location import Location
from main.sample_points_calculator import calculate_intervals


class TestSamplePointsCalculator(TestCase):
    def test_calculate_intervals(self):
        location_one = Location(54.906163, -1.381980, 150, "Fawcett street")
        location_two = Location(51.503532, -0.127796, 150, "10 Downing street")

        expected_latitude_interval = -0.017013155
        expected_longitude_interval = 0.00627092
        actual_latitude, actual_longitude = calculate_intervals(location_one, location_two, 200)
        self.assertEqual((expected_latitude_interval, expected_longitude_interval), (actual_latitude, actual_longitude))
