from unittest import *
from circle import *

class TestCircle(TestCase):
    def init_test(self):
        c1 = Circle(2.0, 10)
        radius, length = c1.radius
