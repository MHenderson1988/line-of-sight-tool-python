# The circle class accepts two arguments, the radius of the circle and the length of arc between the locations
# which are being assessed.  This generates a representation of the Earth's curvature which will be represented on the
# final graph.  This is important to represent as the curvature of the Earth makes a big difference to whether
# or not, line of sight exists between locations.

import numpy as np


class Circle:

    def __init__(self, radius_of_circle, length_of_arc):
        self.radius = radius_of_circle
        self.arc_length = length_of_arc

    # Define Circle class methods

    # Calculate the central angle, in degrees, by using the arc_length
    # Gives angle in degrees at centre of the circle between the two points (beginning and end points of arc_length)
    def calc_degrees(self):
        return (self.arc_length / (np.pi * self.calc_diameter())) * 360

    # Calculate the central angle in radians, between two points on the circle
    def calc_radians(self):  # Where theta is the angle between both points at the centre of the circle
        return np.radians(self.calc_degrees())  # Convert degrees to radians to work with chord_length formula

    # Returns the chord lengths of the arc, taking theta (angle in radians) as it's argument
    # The chord is the horizontal line which separates the arc segment from the rest of the circle
    # Formula for theta (radians) only, not degrees #confirmed using http://www.ambrsoft.com/Trigocalc/Sphere/Arc_.htm
    def calc_chord_length(self):
        return 2 * self.radius * np.sin(self.calc_radians() / 2)

    # Calculates the length of arc, taking theta (angle in radians) as its argument.
    # Confirmed using http://www.ambrsoft.com/Trigocalc/Sphere/Arc_.htm
    def calc_arc_length(self):
        return (self.calc_degrees() / 360) * self.calc_diameter() * np.pi

    # Calculates the Sagitta of the arc segment.  The Sagitta is the distance from the centre of the arc
    # to the centre of the chord
    # Confirmed correct against online calculator https://www.liutaiomottola.com/formulae/sag.htm
    def calc_sagitta(self):
        return self.radius - (np.sqrt((self.radius ** 2) - ((self.calc_chord_length() / 2) ** 2)))

    # Calculate the distance between the chord of the segment and the centre of the circle
    def calc_arc_apothem(self):
        return self.radius - self.calc_sagitta()

    # Calculate centre point of circle
    # x
    def calc_circular_centre_x(self):
        return self.calc_chord_length() / 2

    # Calculate centre point of circle
    # y
    def calc_circular_centre_y(self):
        return self.calc_sagitta() - self.radius

    # Calculate the diameter of the circle
    def calc_diameter(self):
        return self.radius * 2

    # Returns the starting angle of the circular arc
    # Takes two arguments, starting y and x coordinates
    def calc_start_angle(self, start_y, start_x):
        centre_y = self.calc_circular_centre_y()
        centre_x = self.calc_circular_centre_x()
        return np.arctan2(start_y - centre_y, start_x - centre_x)

    # Returns the ending angle of the circular arc
    # Takes two arguments, ending y and x coordinates
    def calc_end_angle(self, end_y, end_x):
        centre_y = self.calc_circular_centre_y()
        centre_x = self.calc_circular_centre_x()
        return np.arctan2(end_y - centre_y, end_x - centre_x)
