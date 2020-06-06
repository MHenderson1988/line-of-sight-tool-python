from unittest import *
from circle import *


class TestCircle(TestCase):
    def test_radius(self):
        c1 = Circle(1, 1)
        self.assertEqual(1, c1.radius)

    def test_arc_length(self):
        c1 = Circle(1, 1)
        self.assertEqual(1,c1.arc_length)

    def test_calc_degrees(self):
        c1 = Circle(1, 1)
        self.assertEqual(57.296, round(c1.calc_degrees(), 3))

    def test_calc_radians(self):
        c1 = Circle(1, 1)
        self.assertEqual(1, c1.calc_radians())

    def test_calc_chord_length(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.959, round(c1.calc_chord_length(), 3))

    def test_calc_arc_length(self):
        c1 = Circle(1, 1)
        self.assertEqual(1, c1.calc_arc_length())

    def test_calc_sagitta(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.122, round(c1.calc_sagitta(),3))

    def test_calc_arc_height(self):
        c1 = Circle(1, 1)
        self.assertEqual(0.878, round(c1.calc_arc_height(), 3))

    def test_calc_circular_centre_x(self):
        c1 = Circle(1,1)
        self.assertEqual(0.479, round(c1.calc_circular_centre_x(),3))

    def test_calc_circular_centre_y(self):
        c1 = Circle(1,1)
        self.assertEqual(-0.878, round(c1.calc_circular_centre_y(),3))

    def test_calc_diameter(self):
        c1 = Circle(1,1)
        self.assertEqual(2, c1.calc_diameter())