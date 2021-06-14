import traceback

from main.classes.arc_solver import ArcSolver
from main.classes.LocationFactory import LocationFactory


class LineOfSight:
    def __init__(self, *args, **kwargs):
        self.locations_1 = LocationFactory.process(args[0])
        self.locations_2 = LocationFactory.process(args[1])
        self.samples = args[2]
        self.distance_units = kwargs.get("distance_units", "NAUTICAL_MILES")
        self.height_units = kwargs.get("height_units", "FEET")
        self.earth_radius = self.earth_radius()

    def earth_radius(self):
        if self.distance_units == "NAUTICAL_MILES":
            return 3440.065
        elif self.distance_units == "MILES":
            return 3958.8
        elif self.distance_units == "KILOMETRES":
            return 6371.0
        else:
            traceback.print_exc()
            return Exception("A unit of distance was not specified or there was a type in the gui/code.  Get help!")

    def get_los(self):
        # Analyse each location in the first .csv of locations
        for loc in self.locations_1:
            # analyse first location with each location in the second .csv of locations
            for loc2 in self.locations_2:
                arc_length = loc.great_circle(loc2)
                pseudo_earth = ArcSolver(self.earth_radius(), arc_length, distance=self.distance_units,
                                         height=self.height_units)
