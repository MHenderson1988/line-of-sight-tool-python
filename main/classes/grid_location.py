# Grid is used for Easting and Northing locations
from abc import ABC

from pyproj import Transformer

from main.classes.decimal_location import DecimalLocation
from main.classes.location import Location


class GridLocation(Location, ABC):

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

    def __str__(self):
        return "{self.name} is a location of easting and northing grid coordinates at northing: {self.y}, easting:" \
               " {self.x}, at a height of {self.height} {self.height_units}".format(self=self)

    def __eq__(self, other):
        return self._y == other.y and self._x == other.x and self._height == other.height

    def to_decimal(self):
        try:
            transformer = Transformer.from_crs('epsg:27700', 'epsg:4326')
            x, y = transformer.transform(self.x, self.y)
            location = DecimalLocation(y, x, self.height, self.name, distance_units=self.distance_units,
                                       height_units=self.height_units)
        except Exception:
            print("An exception occurred when converting a GridLocation to a DecimalLocation")
        return location
