from abc import ABC, abstractmethod


class Location(ABC):
    def __init__(self, *args, **kwargs):
        self._y = args[0]
        self._x = args[1]
        self._height = args[2]
        self.name = args[3]
        self.distance_units = kwargs.get("distance_units", "NAUTICAL MILES")
        self.height_units = kwargs.get("height_units", "FEET")

    @property
    @abstractmethod
    def y(self):
        pass

    @y.setter
    @abstractmethod
    def y(self, value):
        pass

    @property
    @abstractmethod
    def x(self):
        pass

    @x.setter
    @abstractmethod
    def x(self, value):
        pass

    @property
    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass
