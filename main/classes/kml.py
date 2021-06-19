import os

import simplekml

DESKTOP = os.path.expanduser("~/Desktop")


class Kml:
    def __init__(self, *args, **kwargs):
        self.loc1 = args[0]
        self.loc2 = args[1]
        self.kml_obj = simplekml.Kml(open=1)
        self.fol1 = self.kml_obj.newfolder(name=kwargs.get("fol1", "First locations"))
        self.fol2 = self.kml_obj.newfolder(name=kwargs.get("fol2", "Second locations"))
        self.lsfol = self.kml_obj.newfolder(name="LOS vectors")
        self.output_path = kwargs.get('output', DESKTOP)

    """
    Saves the .kml file and returns a message to tell you when complete
    """

    def create(self):
        self.create_points()
        self.create_linestrings()
        save_string = self.output_path + "/LOS analysis.kml"
        self.kml_obj.save(save_string)
        return print(".KML creation complete")

    """
    Creates a point on the kml file for each location supplied
    """

    def create_points(self):
        for i in self.loc1:
            point = self.fol1.newpoint(name=i.name, coords=[(i.x, i.y, i.height)])
            point.altitudemode = simplekml.AltitudeMode.relativetoground
            point.extrude = 1

        for i in self.loc2:
            point = self.fol2.newpoint(name=i.name, coords=[(i.x, i.y, i.height)])
            point.altitudemode = simplekml.AltitudeMode.relativetoground
            point.extrude = 1

    """
    Creates a linestring between each location in each list.  Ie - every location in list one will be connected to each
    location in list 2.
    """

    def create_linestrings(self):
        locs1 = self.loc1
        locs2 = self.loc2

        for i in locs1:
            for j in locs2:
                linestring = self.lsfol.newlinestring(name=i.name + ', ' + j.name)
                linestring.coords = [(i.x, i.y, i.height), (j.x, j.y, j.height)]
                linestring.altitudemode = simplekml.AltitudeMode.relativetoground
