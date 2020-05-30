import numpy as np


class Circle:

    def __init__(self, radius_of_circle, length_of_arc):
        self.radius = radius_of_circle
        self.circumference = 2 * np.pi * self.radius
        self.diameter = self.radius * 2
        self.arc_length = length_of_arc
        self.degrees = self.calc_Degrees()
        self.radians = self.calc_Radians()
        self.chord_length = self.calc_chord_length()
        self.sagitta = self.calc_Sagitta()
        self.arc_height = self.calc_arc_height()
        self.segment_area = self.calc_segment_area()
        self.centre_to_chord = self.calc_centre_to_chord()
        self.xc = self.calc_circular_centre_x()
        self.yc = self.calc_circular_centre_y()

    # Setters and getters for the Circle class (TODO: setters)
    def get_radius(self):
        return self.radius

    def get_circumference(self):
        return self.circumference

    def get_diameter(self):
        return self.diameter

    def get_arc_length(self):
        return self.arc_length

    def get_radians(self):
        return self.radians

    def get_degrees(self):
        return self.degrees

    def get_chord_length(self):
        return self.chord_length

    def get_sagitta(self):
        return self.sagitta

    def get_arc_height(self):
        return self.arc_height

    def get_segment_area(self):
        return self.segment_area

    def get_centre_to_chord(self):
        return self.centre_to_chord

    def get_xc(self):
        return self.xc

    def get_yc(self):
        return self.yc

    # Define Circle class methods

    # calculate the central angle, in degrees, by using the arc_length
    # Gives angle in degrees at centre of the circle between the two points (beginning and end points of arc_length)
    def calc_Degrees(self):
        self.degrees = (self.arc_length / (np.pi * self.diameter)) * 360
        return self.degrees

    # calculate the central angle in radians, between two points on the circle
    def calc_Radians(self):  # Where theta is the angle between both points at the centre of the circle
        self.radians = np.radians(self.degrees)  # Convert degrees to radians to work with chord_length formula
        return self.radians

    # Returns the chord lengths of the arc, taking theta (angle in radians) as it's argument
    # The chord is the horizontal line which separates the arc segment from the rest of the circle
    # Formula for theta (radians) only, not degrees #confirmed using http://www.ambrsoft.com/Trigocalc/Sphere/Arc_.htm
    def calc_chord_length(self):
        self.chord_length = 2 * self.radius * np.sin(self.radians / 2)
        return self.chord_length

    # calculates the length of arc, taking theta (angle in radians) as its argument.
    # Confirmed using http://www.ambrsoft.com/Trigocalc/Sphere/Arc_.htm
    def calc_arc_length(self):
        self.arc_length = (self.degrees / 360) * self.diameter * np.pi
        return self.arc_length

    # calculates the sagitta of the arc segment.  The sagitta is the horizontal line which extends from the bottom
    # of the circle to the chord of the segment
    # Confirmed correct against online calculator https://www.liutaiomottola.com/formulae/sag.htm
    def calc_Sagitta(self):
        self.sagitta = self.radius - (np.sqrt((self.radius ** 2) - ((self.chord_length / 2) ** 2)))
        return self.sagitta

    # calculate the height of the arc
    # Radius - sagitta of the segment
    def calc_arc_height(self):
        self.arc_height = self.radius - self.sagitta
        return self.arc_height

    # calculates the area of the circular segment/arc).
    def calc_segment_area(self):
        self.segment_area = (self.radians - np.sin(self.radians) / 2) * self.radius ** 2
        return self.segment_area

    # calculate the height of the arc showing distance FROM the centre of the circle
    # Radius - sagitta of the segment
    def calc_centre_to_chord(self):
        self.centre_to_chord = self.radius - self.sagitta
        return self.centre_to_chord

    # calculate centre point of circle
    # x
    def calc_circular_centre_x(self):
        self.xc = self.get_chord_length() / 2
        return self.xc

    def calc_circular_centre_y(self):
        self.yc = self.get_sagitta() - self.get_radius()
        return self.yc
