import os
import traceback

import matplotlib.pyplot as plt
import numpy as np

DESKTOP = os.path.expanduser("~/Desktop")


class Graph:
    def __init__(self, *args, **kwargs):
        self.elevation_data = args[0]
        self.loc1 = args[1]
        self.loc2 = args[2]
        self.earth = args[3]
        self.output_path = kwargs.get('output', DESKTOP)
        self.los_line = self.get_los_line()
        self.los_intersect = self.check_intersect()

    """
    Saves an image of the graph which is created using ArcSolver x and y values to draw the curvature of the earth.
    The Y values provided from the elevation data are then overlaid above the ArcSolver data.
    """

    def build(self):
        try:
            assert len(self.earth.y_coordinates) == len(self.elevation_data), \
                "Elevation data sample size does not match earth data sample size."

            los_line = self.get_los_line()

            base_reg = 0
            plt.figure(figsize=(15, 5))
            plt.plot(self.earth.x_coordinates, self.elevation_data)  # Terrain path
            plt.plot(self.earth.x_coordinates, self.earth.y_coordinates)  # Earth curvature path
            plt.plot(self.earth.x_coordinates, los_line, color=self.select_colour())  # Line of sight path
            plt.fill_between(self.earth.x_coordinates, self.elevation_data, base_reg, alpha=0.1)
            plt.text(self.earth.x_coordinates[0], los_line[0], self.loc1.name + ": " + str(self.loc1.height))
            plt.text(self.earth.x_coordinates[-1], los_line[-1], self.loc2.name + ": " + str(self.loc2.height))
            plt.xlabel("Distance (" + self.loc1.distance_units + ")"),
            plt.ylabel("Elevation (" + self.loc1.height_units + ")"),
            plt.grid()
            self.save_file(plt)

            # close the plt to save memory
            plt.close()
        except Exception:
            traceback.print_exc()

    """
    Returns a NDArray of y-axis values which will be used to draw a straight line between the first and second location.
    These values will also be used to look for locations along the path where the terrain data is of a higher value
    at each sample point which indicates terrain is blocking the line of sight.
    """

    def get_los_line(self):
        loc_1 = float(self.loc1.height) + self.elevation_data[0]
        loc_2 = float(self.loc2.height) + self.elevation_data[-1]
        return np.linspace(loc_1, loc_2, len(self.elevation_data))

    """
    Returns true if at the sampled point, the terrain elevation value is greater than the line of sight value between
    two locations.  Returns false if each point is of greater value than the terrain data.
    """

    def check_intersect(self):
        i = 0
        while i < len(self.los_line):
            if self.los_line[i] < self.elevation_data[i]:
                return True
            else:
                i += 1
        return False

    """
    Returns red if LOS line intersects with the terrain data and green if not.
    """

    def select_colour(self):
        if self.los_intersect:
            return 'red'
        else:
            return 'green'

    def save_file(self, a_plt):
        filename = self.loc1.name + ' to ' + self.loc2.name
        if self.los_intersect:
            a_plt.savefig(self.output_path + '/' + filename + " negative LOS")
        else:
            a_plt.savefig(self.output_path + '/' + filename + " positive LOS")
