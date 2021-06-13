# Grid is used for Easting and Northing locations
from abc import ABC

from main.classes.location import Location


class GridLocation(Location, ABC):
    def __str__(self):
        return "{self.name} is a location of easting and northing grid coordinates at northing: {self.y}, easting:" \
               " {self.x}, at a height of {self.height} {self.height_units}".format(self=self)
