import csv
import re
import traceback
from collections import deque

from main.classes.decimal_location import DecimalLocation
from main.classes.grid_location import GridLocation


class LocationFactory:
    def __init__(self, *args, **kwargs):
        self._file = args[0]
        self.distance_units = kwargs.get('distance', "NAUTICAL_MILES")
        self.height_units = kwargs.get('height', "FEET")
        self.locations = self.process_data()

    @property
    def file(self):
        return self._file

    """
    Returns a value error if a file not ending in .csv is supplied.  Else sets the file attribute to the given value
    """

    @file.setter
    def file(self, aFile):
        if aFile.endswith('.csv'):
            self._file = aFile
        else:
            return ValueError("Files must be in .csv format")

    """
    Returns a dequeue of DecimalLocation objects, attributes of which are populated using the appropriate csv headings
    """

    def process_data(self):
        with open(self.file, newline='') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            header = reader.fieldnames
            for words in header:
                if re.match("^[e|E]asting[s]*", words):
                    try:
                        return self.process_osbg(reader)
                    except TypeError:
                        print("A valid DictReader was not provided")
                if re.match("^[l|L]atitude[s]*", words):
                    try:
                        return self.process_decimal(reader)
                    except TypeError:
                        print("A valid DictReader was not provided")

    """
    Returns a deque of DecimalLocation instances.  Attributes are parsed from the .csv file DictReader provided as an
    argument.  
    """

    def process_decimal(self, aReader):
        queue = deque()
        for row in aReader:
            try:
                loc = DecimalLocation(row['latitude'], row['longitude'], row['height'], row['name'],
                                      distance_units=self.distance_units, height_units=self.height_units)
                queue.append(loc)
            except ValueError:
                print("Exception occured creating a DecimalLocation object and appending it to the queue in the"
                      "LocationFactory")
                traceback.print_exc()
        return queue

    """
    Returns a deque of DecimalLocation instances which are created from GridLocations using the to_decimal() method.
    Attributes are parsed from the .csv file DictReader provided as an argument.  
    """

    def process_osbg(self, aReader):
        queue = deque()
        for row in aReader:
            try:
                loc = GridLocation(row['northing'], row['easting'], row['height'], row['name'],
                                   distance_units=self.distance_units, height_units=self.height_units)
                dec_loc = loc.to_decimal()
                queue.append(dec_loc)
            except ValueError:
                print("Exception occured creating a DecimalLocation object and appending it to the queue in the"
                      "LocationFactory")
                traceback.print_exc()
        return queue
