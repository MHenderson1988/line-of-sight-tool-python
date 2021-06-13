from abc import ABC, abstractmethod


class Location(ABC):
    def __init__(self, *args, **kwargs):
        self.y = args[0]
        self.x = args[1]
        self.height = args[2]
        self.name = args[3]
        self.distance_units = kwargs.get("distance_units", "NAUTICAL MILES")
        self.height_units = kwargs.get("height_units", "FEET")

    @abstractmethod
    def __str__(self):
        return '{self.name} is a Location at y: {self.y}, x: {self.x}.  With a height of {self.height}' \
               ' {self.height_units}.'.format(self=self)
