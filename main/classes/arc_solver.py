# The circle class accepts two arguments, the radius of the circle and the length of arc between the locations
# which are being assessed.  This generates a representation of the Earth's curvature which will be represented on the
# final graph.  This is important to represent as the curvature of the Earth makes a big difference to whether
# or not, line of sight exists between locations.
import math
from collections import deque

import numpy as np


class ArcSolver:
    """
    ArcSolver class accepts two required arguments of radius and arc_length (Representing the great circle distance
    between two positions on the perimeter of the circle).  Optional kwargs of sample and distance/height units.
    """

    def __init__(self, *args, **kwargs):
        self.radius = float(args[0])
        self.arc_length = float(args[1])
        self.samples = int(kwargs.get("samples", 150))
        self.distance_units = kwargs.get("distance", "NAUTICAL_MILES")
        self.height_units = kwargs.get("height", "FEET")
        self.radians = self.arc_length / self.radius
        self.chord_length = 2 * self.radius * np.sin(self.radians / 2)
        self.degrees = self.radians * 180 / np.pi
        self.sagitta = float(self.radius - (np.sqrt((self.radius ** 2) - ((self.chord_length / 2) ** 2))))
        self.arc_apothem = self.radius - self.sagitta
        self.circular_centre_x = self.chord_length / 2
        self.circular_centre_y = self.sagitta - self.radius
        self.diameter = self.radius * 2
        self.start_angle = math.atan2(0 - self.circular_centre_y, 0 - self.circular_centre_x)
        self.end_angle = math.atan2(0 - self.circular_centre_y, self.arc_length - self.circular_centre_x)
        self.angles_list = np.linspace(self.start_angle, self.end_angle, self.samples)
        self.x_coordinates = np.linspace(0, self.arc_length, self.samples).tolist()
        self.y_coordinates = self.calculate_earth_surface_y_values()

    """ 
    Returns a numpy array of y-axis values for mapping on matplotlib graph.  x values list is a list of distances
    in NAUTICAL_MILES.  Each y-axis value represents the rising and falling of the earth to simulate 'curvature' which
    effects line of sight visibility.
    """

    def calculate_earth_surface_y_values(self):
        assert self.samples == len(self.x_coordinates)
        y_values_list = deque()
        for j in self.angles_list:
            # Calculate the y axis value (height) for the corresponding x value (distance).  Subtract the apothem
            # of the circle to ensure the arc starts at coordinates 0,0 and ends at zero again on the y axis
            y = self.radius * math.sin(j) - self.arc_apothem
            y = self.convert_y_values(y)
            y_values_list.append(y)

        return y_values_list

    """
    Returns a converted height unit based upon the distance and height units of measurement input by the user.
    This ensures that it will later be represented correctly on any graph software relative to the height units 
    provided for the terrain data.
    """

    def convert_y_values(self, y_value):
        if self.distance_units == "NAUTICAL_MILES":
            if self.height_units == "FEET":
                return y_value * 6076
            if self.height_units == "METRES":
                return y_value * 1852
            else:
                return Exception("Something went wrong converting NAUTICAL_MILES to the selected height units")
        elif self.distance_units == "KILOMETRES":
            if self.height_units == "FEET":
                return y_value * 3281
            if self.height_units == "METRES":
                return y_value * 1000
            else:
                return Exception("Something went wrong converting Kilometres to the selected height units")
        elif self.distance_units == "MILES":
            if self.height_units == "FEET":
                return y_value * 5280
            if self.height_units == "METRES":
                return y_value * 1609.34
        else:
            return Exception("Something went wrong converting y values from the distance units to the height units.")

    """
    Returns true if arc length and radius are identical to another instance
    """

    def __eq__(self, o: object) -> bool:
        if isinstance(o, ArcSolver):
            if (o.radius == self.radius) & (o.arc_length == self.arc_length):
                return True
            return False

    """
    Returns the string value of the object
    """

    def __str__(self) -> str:
        return 'A circle with a radius of {self.radius} and an arc length of {self.arc_length}'.format(self=self)
