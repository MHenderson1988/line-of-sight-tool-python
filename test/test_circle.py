from unittest import TestCase

import numpy as np

from main.circle import Circle


class TestCircle(TestCase):
    def test_radius(self):
        c1 = Circle(1, 1)
        self.assertEqual(1, c1.radius)

    def test_arc_length(self):
        c1 = Circle(1, 1)
        expected = 1 / 1
        self.assertEqual(expected, c1.arc_length)

    def test_calc_degrees(self):
        c1 = Circle(1, 1)
        self.assertEqual(57.29577951308232, c1.calc_degrees())

    def test_calc_radians(self):
        c1 = Circle(1, 1)
        self.assertEqual(1, c1.calc_radians())

    def test_calc_chord_length(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.958851077208406, c1.calc_chord_length())

    def test_calc_arc_length(self):
        c1 = Circle(1, 1)
        self.assertEqual(1, c1.calc_arc_length())

    def test_calc_sagitta(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.12241743810962724, c1.calc_sagitta())

    def test_calc_arc_apothem(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.87758256, c1.calc_arc_apothem())

    def test_calc_circular_centre_x(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.479425538604203, c1.calc_circular_centre_x())

    def test_calc_circular_centre_y(self):
        c1 = Circle(1, 1)
        self.assertEqual(-0.8775825618903728, c1.calc_circular_centre_y())

    def test_calc_diameter(self):
        c1 = Circle(1, 1)
        self.assertEqual(2, c1.calc_diameter())

    def test_calc_start_angle(self):
        c1 = Circle(1, 1)
        self.assertEqual(2.0707963267948966, c1.calc_start_angle(0, 0))

    def test_calc_end_angle(self):
        c1 = Circle(1, 1)
        self.assertEqual(1.0353981633974483, c1.calc_end_angle(0, 1))

    def test_calculate_earth_surface_y_values(self):
        c1 = Circle(1, 1)
        start_angle, end_angle = c1.calc_start_angle(0, 0), c1.calc_end_angle(0, 1)
        x_values = np.linspace(0, 1, 3)
        angles_list = np.linspace(start_angle, end_angle, 3)
        expected_values = [0.0, 226.42703, -32.44148]
        actual_values = c1.calculate_earth_surface_y_values(x_values, angles_list)
        for i in range(len(expected_values)):
            self.assertEqual(expected_values[i], actual_values[i])
