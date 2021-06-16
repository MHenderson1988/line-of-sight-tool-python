import os
import traceback

from main.api_handling.google_handler import GoogleHandler
from main.classes.LocationFactory import LocationFactory
from main.classes.arc_solver import ArcSolver
from main.classes.graph import Graph

DESKTOP = os.path.expanduser("~/Desktop")


class LineOfSight:
    def __init__(self, *args, **kwargs):
        self.locations_1 = LocationFactory(args[0])
        self.locations_2 = LocationFactory(args[1])
        self.samples = kwargs.get("samples", 150)
        self.output_fol = kwargs.get("output", )
        self.distance_units = kwargs.get("distance_units", "NAUTICAL_MILES")
        self.height_units = kwargs.get("height_units", "FEET")
        self.api_key = kwargs.get("key", "NULL")
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
        for loc in self.locations_1.locations:
            # analyse first location with each location in the second .csv of locations
            for loc2 in self.locations_2.locations:
                try:
                    arc_length = loc.great_circle(loc2)
                    handler = GoogleHandler(loc, loc2, key=self.api_key, samples=self.samples,
                                            distance_units=self.distance_units, height_units=self.height_units)
                    pseudo_earth = ArcSolver(self.earth_radius, arc_length, samples=self.samples,
                                             height=self.height_units,
                                             distance=self.distance_units)
                    los_graph = Graph(handler.elevation_data, loc, loc2, pseudo_earth, output=self.output_fol)
                    los_graph.build()
                except Exception:
                    traceback.print_exc()
