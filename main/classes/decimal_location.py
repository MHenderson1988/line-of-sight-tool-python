# Decimal classes is used for decimal latitude and longitude locations
from abc import ABC

from main.classes.location import Location


class DecimalLocation(Location, ABC):
    def __str__(self):
        return "{self.name} is a location of decimal latitude and longitude at latitude: {self.y}, longitude: {self.x}," \
               "at a height of {self.height} {self.height_units}".format(self=self)
