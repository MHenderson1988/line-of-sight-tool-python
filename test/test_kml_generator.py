import os
from unittest import TestCase

from main.kml_generator import initialise_folders, create_points, create_linestrings, create_kml_file
from main.location import Location

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


class TestKmlGenerator(TestCase):
    def test_create_kml_file(self):
        location_list = [(Location(55.55, -1.45, 150, "point1")), (Location(55.55, -1.44, 150, "point2"))]
        location_list_2 = [(Location(54.54, -1.45, 150, "point1_2")), (Location(54.54, -1.44, 150, "point2_2"))]
        create_kml_file(location_list, location_list_2, "Folder 1", "Folder 2", self.create_test_file_path())

    def test_initalise_folders(self):
        kml_object, folder_one, folder_two, line_of_sight_folder = initialise_folders("Location one", "Location two")
        self.assertEqual("Location one", folder_one.name)

    def test_create_points(self):
        location_list = [Location(55.55, -1.45, 150, "point1"), Location(55.54, -1.44, 150, "point2")]
        kml_object, folder_one, folder_two, line_of_sight_folder = initialise_folders("Location one", "Location two")
        list_of_points = create_points(location_list, folder_one)
        self.assertEqual('-1.45,55.55,150', str(list_of_points[0].coords))

    def test_create_linestrings(self):
        kml_object, folder_one, folder_two, line_of_sight_folder = initialise_folders("Location one", "Location two")
        location_list = [(Location(55.55, -1.45, 150, "point1")), (Location(55.55, -1.44, 150, "point2"))]
        location_list_2 = [(Location(54.54, -1.45, 150, "point1_2")), (Location(54.54, -1.44, 150, "point2_2"))]
        linestring_list = create_linestrings(location_list, location_list_2, line_of_sight_folder)
        self.assertEqual("point1, point1_2", str(linestring_list[0].name))

    @staticmethod
    def create_test_file_path():
        return os.path.join(CURRENT_DIR, "data/")
