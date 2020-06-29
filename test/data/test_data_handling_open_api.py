from unittest import TestCase

from main.data_handling_open_api import construct_url_open_elevation, construct_json_post_data
from main.location import Location


class TestDataHandlingOpenApi(TestCase):
    def test_construct_url_open_elevation(self):
        location_one = Location(54.906163, -1.381980, 150, "Fawcett street")
        location_two = Location(51.503532, -0.127796, 150, "10 Downing street")

        print(construct_url_open_elevation(location_one, location_two, 10))

    def test_construct_json_post_data(self):
        location_one = Location(54.906163, -1.381980, 150, "Fawcett street")
        location_two = Location(51.503532, -0.127796, 150, "10 Downing street")

        print(construct_json_post_data(location_one, location_two, 10)
