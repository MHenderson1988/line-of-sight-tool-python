# Grid is used for Easting and Northing locations
from abc import ABC

from pyproj import Transformer

from main.classes.decimal_location import DecimalLocation
from main.classes.non_decimal_location import NonDecimalLocation


class GridLocation(NonDecimalLocation, ABC):

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 999999 < value < -999999:
            exc_str = "%f must be less than %f and greater than %f" % (value, 999999, 999999)
            raise ValueError(exc_str)
        else:
            self._y = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if 999999 < value < -999999:
            exc_str = "%f must be less than %f and greater than %f" % (value, 999999, 999999)
            raise ValueError(exc_str)
        else:
            self._x = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, aHeight):
        self._height = aHeight

    def __str__(self):
        return "{self.name} is a location of easting and northing grid coordinates at northing: {self.y}, easting:" \
               " {self.x}, at a height of {self.height} {self.height_units}".format(self=self)

    def __eq__(self, other):
        return self._y == other.y and self._x == other.x and self._height == other.height

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

    def calculate_interval(self, aObject, samples):
        assert isinstance(aObject, GridLocation), \
            "Error: calculate_interval is only valid with other DecimalLocation objects"
        int_north = (aObject.y - self.y) / samples
        int_east = (aObject.x - self.x) / samples
        return int_north, int_east

    def to_decimal(self):
        try:
            transformer = Transformer.from_crs('epsg:27700', 'epsg:4326')
            y, x = transformer.transform(self.x, self.y)
            aLocation = DecimalLocation(y, x, self.height, self.name, distance_units=self.distance_units,
                                        height_units=self.height_units)
            return aLocation
        except Exception:
            print("An exception occurred when converting a GridLocation to a DecimalLocation")
