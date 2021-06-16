from unittest import TestCase

from main.classes.arc_solver import ArcSolver


class TestCircle(TestCase):
    def setUp(self) -> None:
        self.test = ArcSolver(1, 1, samples=3)

    def test_radians(self):
        self.assertIsInstance(self.test.radians, float)
        self.assertEqual(1, self.test.radians)

    def test_chord_length(self):
        self.assertIsInstance(self.test.chord_length, float)
        self.assertEqual(0.958851077208406, self.test.chord_length)

    def test_degrees(self):
        self.assertIsInstance(self.test.degrees, float)
        self.assertEqual(57.29577951308232, self.test.degrees)

    def test_sagitta(self):
        self.assertIsInstance(self.test.sagitta, float)
        self.assertEqual(0.12241743810962724, self.test.sagitta)

    def test_arc_apothem(self):
        self.assertIsInstance(self.test.arc_apothem, float)
        self.assertEqual(0.8775825618903728, self.test.arc_apothem)

    def test_circular_centre_x(self):
        self.assertIsInstance(self.test.circular_centre_x, float)
        self.assertEqual(0.479425538604203, self.test.circular_centre_x)

    def test_circular_centre_y(self):
        self.assertIsInstance(self.test.circular_centre_y, float)
        self.assertEqual(-0.8775825618903728, self.test.circular_centre_y)

    def test_start_angle(self):
        self.assertIsInstance(self.test.start_angle, float)
        self.assertEqual(2.0707963267948966, self.test.start_angle)

    def test_end_angle(self):
        self.assertIsInstance(self.test.end_angle, float)
        self.assertEqual(1.0353981633974483, self.test.end_angle)

    def test_calculate_earth_surface_y_values(self):
        c1 = ArcSolver(1, 1, samples=3)
        expected_values = [0.0, 742.856702533, -106.43329711369864]
        actual_values = c1.y_coordinates
        for i in range(len(expected_values)):
            self.assertAlmostEqual(expected_values[i], actual_values[i])
