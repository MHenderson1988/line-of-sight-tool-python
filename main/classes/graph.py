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

            filename = self.loc1.name + ' to ' + self.loc2.name
            plt.savefig(self.output_path + '/' + filename)
        except Exception:
            traceback.print_exc()

    def get_los_line(self):
        loc_1 = float(self.loc1.height) + self.elevation_data[0]
        loc_2 = float(self.loc2.height) + self.elevation_data[-1]
        return np.linspace(loc_1, loc_2, len(self.elevation_data))

    def does_intersect(self):
        i = 0
        while i < len(self.los_line):
            if self.los_line[i] < self.elevation_data[i]:
                return True
            else:
                i += 1
        return False

    def select_colour(self):
        if self.does_intersect():
            return 'red'
        else:
            return 'green'
