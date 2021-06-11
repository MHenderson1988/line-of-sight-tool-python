import time

import numpy as np

from main import location_reference_converter, circle, data_handling_google_api
from main.graph_processing import create_graph
from main.kml_generator import create_kml_file
from main.unit_conversion import define_earth_radius, calculate_great_circle_distance
from main.validation_handling import validate_longitude_latitude


def run_graphing_and_kml_process(input_file_one, first_file_type, input_file_two, second_file_type, height_units,
                                 distance_units, output_folder, api_key, samples):
    try:
        # This will have options in future for different units of measurement
        earth_radius = define_earth_radius(distance_units)

        # Create a list of location objects from both .csv files
        first_location_list = location_reference_converter.conversion_type(input_file_one, first_file_type)
        second_location_list = location_reference_converter.conversion_type(input_file_two, second_file_type)

        # Iterate through the locations in the first .csv file
        for i in first_location_list:
            # Retrieve the first Location object and store its coordinates
            assert len(first_location_list) > 0
            pos_1 = (i.latitude, i.longitude)
            # Iterate through the locations in the second .csv file
            for x in second_location_list:
                assert len(second_location_list) > 0
                # Retrieve the second Location object and store its coordinates
                pos_2 = (x.latitude, x.longitude)

                # Validate that both position's lat/long is a valid floating point number.
                validate_longitude_latitude(pos_1[0], pos_1[1])
                validate_longitude_latitude(pos_2[0], pos_2[1])

                # Calculate the great circle distance between both locations using the haversine formula
                great_circle_distance = calculate_great_circle_distance(pos_1, pos_2, distance_units)

                # Create a circle object to simulate curvature of the earth.
                c1 = circle.ArcSolver(earth_radius, great_circle_distance, samples=samples, distance=distance_units,
                                      height=height_units)

                # Construct api url and extract the elevation data
                elevation_data = data_handling_google_api.send_and_receive_data_google_elevation(
                    i.coordinates_lat_long_as_string,
                    x.coordinates_lat_long_as_string,
                    samples, api_key, c1.y_coordinates, c1.height_units)
                create_graph(c1.x_coordinates, c1.y_coordinates, elevation_data, i, x, output_folder,
                             c1.height_units, c1.distance_units)

                # Rest for a moment to prevent the api being bombarded with requests.
                time.sleep(3)

        create_kml_file(first_location_list, second_location_list, "First Locations", "Second Locations", output_folder)
        return "Graphing and .kml processes complete."
    except MemoryError:
        print("Insufficient memory")
    except OverflowError:
        print("Mathematical error, number too large to compute.  Developer - round your output")
    except TypeError:
        print("Type error")
