import matplotlib.pyplot as plt
import numpy as np

from main.unit_conversion import metres_to_feet


# Creates the graph displaying the line of sight analysis between the two points
def create_graph(x_values, y_values, elevation_data, distance, obj_1, obj_2, output_folder, height_units,
                 distance_units):
    # Convert the y (height) values, of the start/end of the line of sight objects, to the user's desired measurement
    if height_units == "Feet":
        start_los = elevation_data[0] + metres_to_feet(float(obj_1.height))
        end_los = elevation_data[-1] + metres_to_feet(float(obj_2.height))
    else:
        start_los = elevation_data[0] + float(obj_1.height)
        end_los = elevation_data[-1] + float(obj_2.height)

    # Create a path of y values for the LOS plot
    los_path = create_los_path(x_values, start_los, end_los)

    # Calculate whether or not the LOS Y values intersect with the terrain y values
    intersection_colour = select_colour(los_path, elevation_data)

    base_reg = 0
    plt.figure(figsize=(15, 5))
    plt.plot(x_values, elevation_data)  # Terrain path
    plt.plot(x_values, y_values)  # Earth curvature path
    plt.plot(x_values, los_path, color=intersection_colour)  # Line of sight path
    plt.fill_between(x_values, elevation_data, base_reg, alpha=0.1)
    plt.text(x_values[0], start_los, obj_1.name + ": " + str(obj_1.height))
    plt.text(x_values[-1], end_los, obj_2.name + ": " + str(obj_2.height))
    plt.xlabel("Distance (" + distance_units + ")"),
    plt.ylabel("Elevation (" + height_units + ")"),
    plt.grid()
    plt.legend(fontsize='small')

    filename = obj_1.name + ' to ' + obj_2.name
    print('Saving  ' + filename + '...')

    plt.savefig(output_folder + '/' + filename)
    plt.close()
    print('Saved.')


"""
This function creates a numpy array for the LOS path.  By creating multiple y values it can be compared with
the elevation data y values.  This allows us to determine whether or not the lines intersect.

Input is the beginning and ending y values.  They are paired with the spaced x-values and the output is an array of y coordinates.
"""


def create_los_path(x_values, y_start, y_end):
    x = x_values
    y = np.linspace(y_start, y_end, len(x))
    return y


"""
This function compares the two sets of y-values with identical x-values and checks for intersections between the lines.
If an intersection exists then it returns true, else false. 
"""


def does_intersect(los_y, terrain_y):
    i = 0
    intercept = False
    while i < len(los_y):
        if los_y[i] < terrain_y[i]:
            intercept = True
            i += 1
        else:
            i += 1
    return intercept


"""
This takes an input of true or false intercept and outputs a colour - red for blocked LOS and green for clear view
"""


def select_colour(los_y, terrain_y):
    intersection_exists = does_intersect(los_y, terrain_y)
    colour = 'green'
    if intersection_exists:
        colour = 'red'
    return colour
