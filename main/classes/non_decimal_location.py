from abc import ABC, abstractmethod

from main.classes.location import Location


class NonDecimalLocation(Location, ABC):
    class Location(ABC):

        @abstractmethod
        def to_decimal(self):
            pass
