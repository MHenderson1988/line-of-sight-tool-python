from main.graph_processing import earth_curve_y_axis
from main.line_of_sight_calculations import calc_start_angle, calc_end_angle
from unittest import TestCase
from main.circle import Circle
import numpy as np

class TestGraphProcessing(TestCase):
    def test_earth_curve_y_axis(self):
        earth_radius = 3440.065
        arc_length = 80
        circle_object = Circle(earth_radius, arc_length)
        xc, yc = circle_object.calc_circular_centre_x(), circle_object.calc_circular_centre_y()
        x1, y1 = 0, 0
        x2, y2 = arc_length, 0

        x_values = np.linspace(x1, x2, 10)
        print(x_values)
        start_angle = calc_start_angle(y1, yc, x1, xc)
        end_angle = calc_end_angle(y2, yc, x2, xc)
        angle_list = np.linspace(start_angle, end_angle, 10)
        print(start_angle)
        print(end_angle)
        print(angle_list)
        print(earth_curve_y_axis(x_values,earth_radius,angle_list,circle_object) * 1852)