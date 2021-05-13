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
                c1 = circle.Circle(earth_radius, great_circle_distance)

                # Set start and end points for representation of the earths curvature
                x1, y1 = 0, 0
                x2, y2 = great_circle_distance, 0
                angle_list = np.linspace(c1.calc_start_angle(0, 0), c1.calc_end_angle(0, great_circle_distance),
                                         samples)

                x_values = np.linspace(x1, x2, samples)

                # Create the y-axis values to draw the earth's curved surface
                y_values = c1.calculate_earth_surface_y_values(x_values, angle_list, height_units, distance_units)

                # Construct api url and extract the elevation data
                elevation_data = data_handling_google_api.send_and_receive_data_google_elevation(
                    i.coordinates_lat_long_as_string,
                    x.coordinates_lat_long_as_string,
                    samples, api_key, y_values, height_units)
                create_graph(x_values, y_values, elevation_data, i, x, output_folder,
                             height_units, distance_units)

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
