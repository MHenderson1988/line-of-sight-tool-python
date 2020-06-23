import matplotlib.pyplot as plt
import numpy as np


# Returns a numpy array containing the y-axis values for the curvature of the earth
def earth_curve_y_axis(list_of_x_axis_values, earth_radius, list_of_angles, circle_object):
    y_values_list = []
    for j in range(len(list_of_x_axis_values)):
        y = earth_radius * np.sin(list_of_angles[j]) - circle_object.calc_arc_apothem()
        y = y * 1852 # Convert nautical miles to meters for elevation
        y_values_list.append(y)
    y_values_np = np.array(y_values_list)

    return y_values_np


# Creates the graph displaying the line of sight analysis between the two points
def create_graph(x_values, y_values, elevation_data, distance, obj_1, obj_2, output_folder):
    min_elev = min(elevation_data)
    mean_elev = round((sum(elevation_data) / len(elevation_data)), 3)
    max_elev = max(elevation_data)

    start_los = elevation_data[0] + float(obj_1.height)
    end_los = elevation_data[-1] + float(obj_2.height)

    base_reg = 0
    plt.figure(figsize=(10, 4))
    plt.plot(x_values, elevation_data)
    plt.plot(x_values, y_values)
    plt.plot([0, distance], [min_elev, min_elev], '--g', label='min: ' + str(min_elev) + ' m')
    plt.plot([0, distance], [max_elev, max_elev], '--r', label='max: ' + str(max_elev) + ' m')
    plt.plot([0, distance], [mean_elev, mean_elev], '--y', label='ave: ' + str(mean_elev) + ' m')
    plt.plot([0, distance], [start_los, end_los])  # Line of sight line
    plt.fill_between(x_values, elevation_data, base_reg, alpha=0.1)
    plt.text(x_values[0], elevation_data[0], obj_1.name)
    plt.text(x_values[-1], elevation_data[-1], obj_2.name)
    
    plt.xlabel("Distance (Nm)")
    plt.ylabel("Elevation(Meters)"),
    plt.grid()
    plt.legend(fontsize='small')

    filename = obj_1.name + ' to ' + obj_2.name
    print('Saving  ' + filename + '...')

    plt.savefig(output_folder + '/' + filename)
    plt.close()
    print('Saved.')
