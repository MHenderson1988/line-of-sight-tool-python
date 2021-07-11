from unittest import TestCase

from main.classes.arc_solver import ArcSolver
from main.classes.decimal_location import DecimalLocation
from main.classes.graph import Graph


class TestGraph(TestCase):
    def setUp(self) -> None:
        self.test_data = [10, 20, 30]
        self.test_data2 = [900, 2000, 1000]

        self.test_loc = DecimalLocation(55.111, -4.111, 2, "Test1")
        self.test_loc2 = DecimalLocation(44.111, 5.111, 2, "Test2")

        self.test_loc3 = DecimalLocation(55.111, -4.111, 50, "Test1")
        self.test_loc4 = DecimalLocation(44.111, 5.111, 50, "Test2")

        self.test_arc = ArcSolver(3440.065, self.test_loc.great_circle(self.test_loc2))

        self.graph = Graph(self.test_data, self.test_loc, self.test_loc2, 3)
        self.graph2 = Graph(self.test_data2, self.test_loc3, self.test_loc4, 3)

    def test_get_los_line(self):
        actual = self.graph.get_los_line()
        expected = [12, 22, 32]
        i = 0
        while i < len(actual):
            self.assertEqual(expected[i], actual[i])
            i += 1

    def test_does_intersect(self):
        self.assertFalse(self.graph.check_intersect())
        self.assertTrue(self.graph2.check_intersect())

    def test_select_colour(self):
        self.assertEqual('green', self.graph.select_colour())
        self.assertEqual('red', self.graph2.select_colour())
