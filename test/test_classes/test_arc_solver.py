from unittest import TestCase

from main.classes.arc_solver import ArcSolver


class TestCircle(TestCase):
    def setUp(self) -> None:
        self.test = ArcSolver(1, 1, samples=3)
        self.string_test = ArcSolver("1", "1", samples="3")
        self.test_list = [self.test, self.string_test]

    def test_radians(self):
        for test in self.test_list:
            self.assertIsInstance(test.radians, float)
            self.assertEqual(1, test.radians)

    def test_chord_length(self):
        for test in self.test_list:
            self.assertIsInstance(test.chord_length, float)
            self.assertEqual(0.958851077208406, test.chord_length)

    def test_degrees(self):
        for test in self.test_list:
            self.assertIsInstance(self.test.degrees, float)
            self.assertEqual(57.29577951308232, test.degrees)

    def test_sagitta(self):
        for test in self.test_list:
            self.assertIsInstance(test.sagitta, float)
            self.assertEqual(0.12241743810962724, test.sagitta)

    def test_arc_apothem(self):
        for test in self.test_list:
            self.assertIsInstance(test.arc_apothem, float)
            self.assertEqual(0.8775825618903728, test.arc_apothem)

    def test_circular_centre_x(self):
        for test in self.test_list:
            self.assertIsInstance(test.circular_centre_x, float)
            self.assertEqual(0.479425538604203, test.circular_centre_x)

    def test_circular_centre_y(self):
        for test in self.test_list:
            self.assertIsInstance(test.circular_centre_y, float)
            self.assertEqual(-0.8775825618903728, test.circular_centre_y)

    def test_start_angle(self):
        for test in self.test_list:
            self.assertIsInstance(test.start_angle, float)
            self.assertEqual(2.0707963267948966, test.start_angle)

    def test_end_angle(self):
        for test in self.test_list:
            self.assertIsInstance(test.end_angle, float)
            self.assertEqual(1.0353981633974483, test.end_angle)

    def test_calculate_earth_surface_y_values(self):
        for test in self.test_list:
            expected_values = [0.0, 742.856702533, -106.43329711369864]
            actual_values = test.y_coordinates
            for i in range(len(expected_values)):
                self.assertAlmostEqual(expected_values[i], actual_values[i])
