import time

import numpy as np
from haversine import haversine, Unit

from main import location_reference_converter, line_of_sight_calculations, circle, data_handling
from main.graph_processing import earth_curve_y_axis, create_graph
from main.validation_handling import validate_google_sample_number
from main.kml_generator import create_kml_file


def run_program(input_file_one, input_file_two, output_folder, check_box, api_key, samples, first_file_type,
                second_file_type):
    # This will have options in future for different units of measurement
    earth_radius = 3440.065  # in nm

    # Validate the number of samples requested
    validate_google_sample_number(samples)

    # Create a list of location objects from both .csv files
    first_location_list = location_reference_converter.conversion_type(input_file_one, first_file_type)
    second_location_list = location_reference_converter.conversion_type(input_file_two, second_file_type)

    # Iterate through the locations in the first .csv file
    for i in first_location_list:
        # Retrieve the first Location object and store its coordinates
        pos_1 = (i.latitude, i.longitude)
        # Iterate through the locations in the second .csv file
        for x in second_location_list:
            # Retrieve the second Location object and store its coordinates
            pos_2 = (x.latitude, x.longitude)
            # Calculate the great circle distance between both locations using the haversine formula
            # Currently this is returned in Nm but future functionality will allow other values
            great_circle_distance = haversine(pos_1, pos_2, unit=Unit.NAUTICAL_MILES)

            # Create a circle object to simulate curvature of the earth.
            c1 = circle.Circle(earth_radius, great_circle_distance)
            xc, yc = c1.calc_circular_centre_x(), c1.calc_circular_centre_y()

            # Set start and end points for representation of the earths curvature
            x1, y1 = 0, 0
            x2, y2 = great_circle_distance, 0

            start_angle = line_of_sight_calculations.calc_start_angle(y1, yc, x1, xc)
            end_angle = line_of_sight_calculations.calc_end_angle(y2, yc, x2, xc)
            angle_list = np.linspace(start_angle, end_angle, samples)

            x_values = np.linspace(x1, x2, samples)

            # Create the y-axis values to draw the earth's curved surface
            y_values = earth_curve_y_axis(x_values, earth_radius, angle_list, c1)

            # Construct api url and extract the elevation data
            elevation_data = data_handling.send_and_receive_data(i.coordinates_string, x.coordinates_string, samples, api_key,
                                                                 y_values)
            create_graph(x_values, y_values, elevation_data, great_circle_distance, i, x, output_folder)

            # Rest for a moment to prevent the api being bombarded with requests.
            time.sleep(2)

    if check_box == "kml_true":
        create_kml_file(first_location_list, second_location_list, "First Locations", "Second Locations")
    else:
        return "Complete"
