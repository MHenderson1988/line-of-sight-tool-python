# Decimal classes is used for decimal latitude and longitude locations
import traceback
from abc import ABC
from collections import deque

from haversine import haversine, Unit

from main.classes.location import Location


class DecimalLocation(Location, ABC):
    @property
    def y(self):
        return self._y

    """
    Sets the value of the y coordinate to the value provided.  Will attempt to cast non-floating point numbers
    """

    @y.setter
    def y(self, value):
        if 90.0 < value < -90.0:
            exc_str = "%f must be less than %f and greater than %f" % (value, 90.0, -90.0)
            raise ValueError(exc_str)
        else:
            if isinstance(value, float):
                self._y = value
            else:
                try:
                    self._y = float(value)
                except ValueError:
                    traceback.print_exc()
                    print("y must be a floating point number or castable type.")

    @property
    def x(self):
        return self._x

    """
    Sets the x coordinate to the desired value.  If not a floating point number will attempt to cast or throw an
    exception if the value is not castable.
    """

    @x.setter
    def x(self, value):
        if 180.0 < value < -180.0:
            exc_str = "%f must be less than %f and greater than %f" % (value, 180.0, -180.0)
            raise ValueError(exc_str)
        else:
            if isinstance(value, float):
                self._y = value
            else:
                try:
                    self._y = float(value)
                except ValueError:
                    traceback.print_exc()
                    print("X must be a floating point number or other castable type.")

    @property
    def height(self):
        return self._height

    """
    Sets the height to the specified floating point number.  If a floating point number is not provided it will attempt
    to cast to float.  Throws an exception if the type is not castable.
    """

    @height.setter
    def height(self, aHeight):
        if isinstance(aHeight, float):
            self._height = aHeight
        else:
            try:
                self._height = float(aHeight)
            except ValueError:
                traceback.print_exc()
                print("Height must be a floating point number or other castable type.")

    """
    Returns a string representation of the object, including the name, y and x coordinates and the height with
    specified units.
    """

    def __str__(self):
        return "{self.name} is a location of decimal latitude and longitude at latitude: {self.y}, longitude: {self.x}," \
               "at a height of {self.height} {self.height_units}".format(self=self)

    """
    Returns true when compared to another decimal location with identical y and x coordinates and height.
    """

    def __eq__(self, other):
        return self._y == other.y and self._x == other.x and self._height == other.height

    """
    Returns the incremental value of the difference between two sets of decimal degree coordinates.  This is found by
    subtracting the instances latitude and longitude from the object passed as the argument.  Accepts another 
    DecimalLocation object as it's argument or throws an AttributeError
    """

    def calculate_interval(self, aObject, samples):
        try:
            int_lat = (aObject.y - self.y) / samples
            int_lon = (aObject.x - self.x) / samples
            return int_lat, int_lon
        except TypeError:
            traceback.print_exc()
            print("calculate_interval() only must have a valid DecimalLocation object passed as it's argument.")

    """
    Converts the objects height attribute to another value depending on the supplied height_units upon creation.
    """

    def convert_height(self):
        if self.distance_units == "NAUTICAL_MILES":
            if self.height_units == "FEET":
                self._height = self._height * 6076
            if self.height_units == "METRES":
                self._height = self._height * 1852
            else:
                return Exception("Something went wrong converting NAUTICAL_MILES to the selected height units")
        elif self.distance_units == "KILOMETRES":
            if self.height_units == "FEET":
                self._height = self._height * 3281
            if self.height_units == "METRES":
                self._height = self._height * 1000
            else:
                return Exception("Something went wrong converting Kilometres to the selected height units")
        elif self.distance_units == "MILES":
            if self.height_units == "FEET":
                self._height = self._height * 5280
            if self.height_units == "METRES":
                self._height = self._height * 1609.34
        else:
            return Exception(
                "Something went wrong converting y values from the distance units to the height units.")

    """
    Returns a queue of coordinates in decimal degree format.  These are sampled at evenly distributed distances on the
    path between the object and the other DecimalLocation object which is passed as it's argument.  
    
    Note - this currently isn't used in the running of application due to the 'path' function supplied by Google
    Elevation API however it was included as a means to an end should it ever need to be utilised.
    """

    def populate_path(self, aObject, samples):
        try:
            y_int, x_int = self.calculate_interval(aObject, samples)
            queue = deque([(self.y, self.x)])
            for i in range(samples):
                new_y, new_x = round((queue[-1][0] + y_int), 6), round((queue[-1][1] + x_int), 6)
                queue.append((new_y, new_x))
            return queue
        except TypeError:
            traceback.print_exc()
            print("populate_path() accepts only valid DecimalDegree instances as it's argument.")

    """
    Returns a floating point number representing the great circle distance between the object and the argument.  
    Only accepts valid DecimalLocation objects as it's argument.
    """

    # Returns the great circle distance between the two DecimalLocations.  Used to create the arc_length of the
    # ArcSolver class.  Distance units are calculated using the calling objects value.
    def great_circle(self, aObject):
        try:
            return haversine((float(self.y), float(self.x)), (float(aObject.y), float(aObject.x)),
                             unit=Unit.__getattr__(self.distance_units))
        except TypeError:
            traceback.print_exc()
            print("great_circle() only accepts valid DecimalLocation objects as it's argument.")
