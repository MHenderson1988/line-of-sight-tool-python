from unittest import TestCase
from validation_handling import *


class TestValidationHandling(TestCase):
    def test_validate_longitude_latitude_type(self):
        self.assertRaises(TypeError, validate_longitude_latitude, "Hello", 44.444)

    def test_validate_longitude_latitude_value(self):
        self.assertRaises(ValueError, validate_longitude_latitude, 999.999, 55.555)

