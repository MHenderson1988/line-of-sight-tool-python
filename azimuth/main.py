import grid_converter
import line_of_sight_calculations
import data_handling
import numpy as np
import time
import circle

from haversine import haversine, Unit
from graph_processing import *


def run_program(input_file_one, input_file_two, output_folder, api_key, samples):
    # Variables
    earth_radius = 3440.065  # in nm

    # Create a list of location objects from both .csv files
    first_location_list = grid_converter.convert_grids(input_file_one)
    second_location_list = grid_converter.convert_grids(input_file_two)

    # Calculate great circle distance between points
    # To add functionality for difference units of measurement
    for i in first_location_list:
        pos_1 = (i.latitude, i.longitude)
        for x in second_location_list:
            pos_2 = (x.latitude, x.longitude)
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
            y_value_list = []

            # Create the y-axis values to draw the earth's curved surface
            for j in range(len(x_values)):
                y = earth_radius * np.sin(angle_list[j]) - c1.calc_arc_height()
                y = y * 1852  # convert nautical miles to meters
                y_value_list.append(y)

            y_values = np.array(y_value_list)

            # Construct api url and extract the elevation data
            url_construct = data_handling.send_request_google_elevation(i.coordinates, x.coordinates, api_key, samples)
            print("Sending request...")
            received_data = data_handling.receive_request_google_elevation(url_construct)
            print("Receiving data...")
            elevation_data = data_handling.process_response(received_data, y_values)
            print("Extracting data...")

            print("Plotting graph...")
            create_graph(x_values, y_values, elevation_data, great_circle_distance, i, x, output_folder)

            print('Saved...')
            time.sleep(3)
