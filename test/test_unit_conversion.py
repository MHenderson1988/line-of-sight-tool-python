from unittest import TestCase

from main.unit_conversion import get_user_selected_unit_and_convert_distance, get_user_selected_unit_and_convert_height,\
    convert_nm_to_meters, convert_nm_to_feet, convert_nm_to_miles, convert_nm_to_km, convert_meters_to_feet


class TestUnitConversion(TestCase):
    def test_get_user_selected_unit_and_convert_distance(self):
        input_value = 1
        unit_to_convert_to = 'Km'
        self.assertEqual(1.852, get_user_selected_unit_and_convert_distance(input_value, unit_to_convert_to))

    def test_get_user_selected_unit_and_convert_height(self):
        input_value = 1
        unit_to_convert_to = "Feet"
        self.assertEqual(3.28084, get_user_selected_unit_and_convert_height(input_value, unit_to_convert_to))

    def test_convert_meters_to_feet(self):
        input_value = 1
        self.assertEqual(3.28084, convert_meters_to_feet(input_value))

    def test_convert_nm_to_meters(self):
        input_value = 1
        self.assertEqual(1852, convert_nm_to_meters(input_value))

    def test_convert_nm_to_km(self):
        input_value = 1
        self.assertEqual(1.852, convert_nm_to_km(input_value))

    def test_convert_nm_to_miles(self):
        input_value = 1
        self.assertEqual(1.15078, convert_nm_to_miles(input_value))

    def test_convert_nm_to_feet(self):
        input_value = 1
        self.assertEqual(6076.12, convert_nm_to_feet(input_value))
