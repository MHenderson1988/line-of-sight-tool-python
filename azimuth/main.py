import grid_converter
import line_of_sight_calculations
import data_processing
import numpy as np
import time
import circle

from haversine import haversine, Unit
from graph_creator import *

# Variables
earth_radius = 3440.065  # in nm
key = #Your key here, in single quotations ' '
samples = 10
circle_list = []

# Create a list of location objects from both .csv files
# File one
first_location_list = grid_converter.convert_grids_xy('../inputdata/grid.csv')

# File two
second_location_list = grid_converter.convert_grids('../inputdata/radars.csv')

# Calculate great circle distance between points
# To add functionality for difference units of measurement

for i in first_location_list:
    pos_1 = (i.latitude, i.longitude)
    for x in second_location_list:
        pos_2 = (x.latitude, x.longitude)
        great_circle_distance = haversine(pos_1, pos_2, unit=Unit.NAUTICAL_MILES)

        # Create a circle object to simulate curvature of the earth.
        c1 = circle.Circle(earth_radius, great_circle_distance)
        xc = c1.get_xc()
        yc = c1.get_yc()
        position_height = i.height
        position_2_height = x.height

        # Set start and end points for representation of the earths curvature
        x1, y1 = 0, 0
        x2, y2 = great_circle_distance, 0
        start_angle = line_of_sight_calculations.calc_start_angle(y1, yc, x1, xc)
        end_angle = line_of_sight_calculations.calc_end_angle(y2, yc, x2, xc)
        angle_list = np.linspace(start_angle, end_angle, samples)
        x_values = np.linspace(x1, x2, samples)
        y_value_list = []

        for j in range(len(x_values)):
            y = earth_radius * np.sin(angle_list[j]) - c1.get_arc_height()
            y = y * 1852  # convert nautical miles to meters
            y_value_list.append(y)

        y_values = np.array(y_value_list)

        # Construct api url and extract the elevation data
        url_construct = data_processing.send_request_google_elevation(i.coordinates, x.coordinates, key, samples)
        print("Sending request...")
        received_data = data_processing.receive_request_google_elevation(url_construct)
        print("Receiving data...")
        elevation_data = data_processing.process_response(received_data)
        print("Extracting data...")

        print("Plotting graph...")
        create_graph(x_values, y_values, elevation_data, great_circle_distance, i, x)

        print('Saved...')
        time.sleep(3)