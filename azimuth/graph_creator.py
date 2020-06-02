import matplotlib.pyplot as plt


def calculate_mean_elevation(elevation_data):
    return round((sum(elevation_data) / len(elevation_data)), 3)


def calculate_minimum_elevation(elevation_data):
    return min(elevation_data)


def calculate_maximum_elevation(elevation_data):
    return max(elevation_data)


def create_graph(x_values, y_values, elevation_data, distance, obj_1, obj_2):
    min_elev = calculate_maximum_elevation(elevation_data)
    mean_elev = calculate_mean_elevation(elevation_data)
    max_elev = calculate_minimum_elevation(elevation_data)

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
    plt.xlabel("Distance(Nm)")
    plt.ylabel("Elevation(m)")
    plt.grid()
    plt.legend(fontsize='small')

    print('Saving...')

    filename = obj_1.name + ' to ' + obj_2.name

    plt.savefig('../output/' + filename)
    plt.close()