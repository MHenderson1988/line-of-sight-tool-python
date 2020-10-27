from unittest import TestCase

import numpy as np
import numpy.testing as nptest

from main.graph_processing import create_los_path, does_intersect, select_colour


class TestGraphProcessing(TestCase):
    def test_create_los_path(self):
        test_x_values = [1, 2, 3, 4]
        test_y_start = 0
        test_y_end = 12
        expected = np.array([0, 4, 8, 12])
        actual = create_los_path(test_x_values, test_y_start, test_y_end)
        nptest.assert_equal(expected, actual)

    def test_does_intersect(self):
        test_y_los = [1, 2, 3, 4]
        test_y_terrain = [0, 0, 0, 8]
        expected = True
        actual = does_intersect(test_y_los, test_y_terrain)
        self.assertEqual(expected, actual)

    def test_select_colour(self):
        test_y_los = [1, 2, 3, 4]
        test_y_terrain = [0, 0, 0, 8]
        expected = 'red'
        actual = select_colour(test_y_los, test_y_terrain)
        self.assertEqual(expected, actual)
