from unittest import *
from line_of_sight_calculations import *


class TestLineOfSightCalculations(TestCase):
    def test_calc_start_angle(self):
        angle = calc_start_angle(24, 0, 0, 0)
        print(angle)
        self.assertEqual(1.5707963267948966, angle)

    def test_calc_end_angle(self):
        angle = calc_end_angle(0,0,0,0)
        print(angle)
        self.assertEqual(0, angle)