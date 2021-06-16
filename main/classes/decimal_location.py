# Decimal classes is used for decimal latitude and longitude locations
from abc import ABC
from collections import deque

from haversine import haversine, Unit

from main.classes.location import Location


class DecimalLocation(Location, ABC):
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 90.0 < value < -90.0:
            exc_str = "%f must be less than %f and greater than %f" % (value, 90.0, -90.0)
            raise ValueError(exc_str)
        else:
            self._y = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if 180.0 < value < -180.0:
            exc_str = "%f must be less than %f and greater than %f" % (value, 180.0, -180.0)
            raise ValueError(exc_str)
        else:
            self._y = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, aHeight):
        self._height = aHeight

    def __str__(self):
        return "{self.name} is a location of decimal latitude and longitude at latitude: {self.y}, longitude: {self.x}," \
               "at a height of {self.height} {self.height_units}".format(self=self)

    def __eq__(self, other):
        return self._y == other.y and self._x == other.x and self._height == other.height

    # Method which returns the lat/long interval between the object and another decimal_location.
    def calculate_interval(self, aObject, samples):
        int_lat = (aObject.y - self.y) / samples
        int_lon = (aObject.x - self.x) / samples
        return int_lat, int_lon

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

    # Returns a queue of y, x values which represent the sampled points between the two locations
    def populate_path(self, aObject, samples):
        assert isinstance(aObject, DecimalLocation), \
            "Error: calculate_interval is only valid with other DecimalLocation objects"
        y_int, x_int = self.calculate_interval(aObject, samples)
        queue = deque([(self.y, self.x)])
        for i in range(samples):
            new_y, new_x = round((queue[-1][0] + y_int), 6), round((queue[-1][1] + x_int), 6)
            queue.append((new_y, new_x))
        return queue

    # Returns the great circle distance between the two DecimalLocations.  Used to create the arc_length of the
    # ArcSolver class.  Distance units are calculated using the calling objects value.
    def great_circle(self, aObject):
        return haversine((float(self.y), float(self.x)), (float(aObject.y), float(aObject.x)),
                         unit=Unit.__getattr__(self.distance_units))
