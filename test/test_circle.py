from unittest import TestCase

import numpy as np

from main.circle import ArcSolver


class TestCircle(TestCase):
    def test_calc_start_angle(self):
        c1 = ArcSolver(1, 1, samples=3)
        self.assertEqual(2.0707963267948966, c1.start_angle())

    def test_calc_end_angle(self):
        c1 = ArcSolver(1, 1, samples=3)
        self.assertEqual(1.0353981633974483, c1.end_angle())

    def test_calculate_earth_surface_y_values(self):
        c1 = ArcSolver(1, 1, samples=3, height="FEET", distance="NAUTICAL MILES")
        x_values = np.linspace(0, 1, 3)
        angles_list = np.linspace(c1.start_angle, c1.end_angle, 3)
        expected_values = [1.0000000e-05, 7.4285671e+02, -1.0643329e+02]
        actual_values = c1.calculate_earth_surface_y_values()
        for i in range(len(expected_values)):
            self.assertEqual(expected_values[i], actual_values[i])
