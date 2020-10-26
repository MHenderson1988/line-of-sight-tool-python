import matplotlib.pyplot as plt

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

    base_reg = 0
    plt.figure(figsize=(15, 5))
    plt.plot(x_values, elevation_data)
    plt.plot(x_values, y_values)
    plt.plot([0, distance], [start_los, end_los])  # Line of sight line
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
