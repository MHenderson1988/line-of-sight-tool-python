# Decimal classes is used for decimal latitude and longitude locations
from abc import ABC

from main.classes.location import Location


class DecimalLocation(Location, ABC):

    @Location.y.setter
    def y(self, value):
        if 90.0 < value < -90.0:
            exc_str = "%f must be less than %f and greater than %f" % (value, 90.0, -90.0)
            raise ValueError(exc_str)
        else:
            self._y = value

    @Location.x.setter
    def x(self, value):
        if 180.0 < value < -180.0:
            exc_str = "%f must be less than %f and greater than %f" % (value, 180.0, -90.0)
            raise ValueError(exc_str)
        else:
            self._x = value

    def __str__(self):
        return "{self.name} is a location of decimal latitude and longitude at latitude: {self.y}, longitude: {self.x}," \
               "at a height of {self.height} {self.height_units}".format(self=self)
