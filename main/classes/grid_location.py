# Grid is used for Easting and Northing locations
import traceback
from abc import ABC

from pyproj import Transformer

from main.classes.decimal_location import DecimalLocation
from main.classes.non_decimal_location import NonDecimalLocation


class GridLocation(NonDecimalLocation, ABC):

    @property
    def y(self):
        return self._y

    """
    Sets Y attribute to the provided value.  Checks that Y is within a valid range.  If so checks the value is either
    int or a valid castable type.
    """

    @y.setter
    def y(self, value):
        if 999999 < value < -999999:
            exc_str = "%f must be less than %f and greater than %f" % (value, 999999, 999999)
            raise ValueError(exc_str)
        else:
            if isinstance(value, int):
                self._y = value
            else:
                try:
                    self._y = int(value)
                except ValueError:
                    traceback.print_exc()
                    print("Y accepts value of type int or other castable type")

    @property
    def x(self):
        return self._x

    """
    Sets X attribute to the provided value.  Checks that X is within a valid range.  If so checks the value is either
    int or a valid castable type.
    """

    @x.setter
    def x(self, value):
        if 999999 < value < -999999:
            exc_str = "%f must be less than %f and greater than %f" % (value, 999999, 999999)
            raise ValueError(exc_str)
        else:
            if isinstance(value, int):
                self._x = value
            else:
                try:
                    self._x = int(value)
                except ValueError:
                    traceback.print_exc()
                    print("X accepts value of type int or other castable type")

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
    Returns a string representation of the object
    """

    def __str__(self):
        return "{self.name} is a location of easting and northing grid coordinates at northing: {self.y}, easting:" \
               " {self.x}, at a height of {self.height} {self.height_units}".format(self=self)

    """
    Returns true if compared against another object with matching x, y and height attributes
    """

    def __eq__(self, other):
        return self._y == other.y and self._x == other.x and self._height == other.height

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
    Returns the incremental value of the difference between two sets of decimal degree coordinates.  This is found by
    subtracting the instances latitude and longitude from the object passed as the argument.  Accepts another 
    DecimalLocation object as it's argument or throws an AttributeError
    """

    def calculate_interval(self, aObject, samples):
        assert isinstance(aObject, GridLocation), \
            "Error: calculate_interval is only valid with other DecimalLocation objects"
        int_north = (aObject.y - self.y) / samples
        int_east = (aObject.x - self.x) / samples
        return int_north, int_east

    """
    Returns a DecimalLocation object with translated x, y coordinates using pyproj.  
    """

    def to_decimal(self):
        try:
            transformer = Transformer.from_crs('epsg:27700', 'epsg:4326')
            y, x = transformer.transform(self.x, self.y)
            aLocation = DecimalLocation(y, x, self.height, self.name, distance_units=self.distance_units,
                                        height_units=self.height_units)
            return aLocation
        except Exception:
            traceback.print_exc()
            print("An exception occurred when converting a GridLocation to a DecimalLocation")
