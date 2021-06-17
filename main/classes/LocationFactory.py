import csv
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

    @file.setter
    def file(self, aFile):
        if aFile.endswith('.csv'):
            self._file = aFile
        else:
            traceback.print_exc()
            return ValueError("Files must be in .csv format")

    def process_data(self):
        with open(self.file, newline='') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            header = reader.fieldnames
            for words in header:
                try:
                    if words == 'easting':
                        return self.process_osbg(reader)
                    if words == 'latitude':
                        return self.process_decimal(reader)
                except Exception:
                    return ValueError("Did not detect OSBG or Decimal Latitude/Longitude.  Please check headers are"
                                      "correctly labelled in the .csv file supplied")
                    traceback.print_exc()

    def process_decimal(self, aReader):
        queue = deque()
        for row in aReader:
            try:
                loc = DecimalLocation(row['latitude'], row['longitude'], row['height'], row['name'],
                                      distance_units=self.distance_units, height_units=self.height_units)
                queue.append(loc)
            except Exception:
                print("Exception occured creating a DecimalLocation object and appending it to the queue in the"
                      "LocationFactory")
                traceback.print_exc()
        return queue

    def process_osbg(self, aReader):
        queue = deque()
        for row in aReader:
            try:
                loc = GridLocation(row['northing'], row['easting'], row['height'], row['name'],
                                   distance_units=self.distance_units, height_units=self.height_units)
                dec_loc = loc.to_decimal()
                queue.append(dec_loc)
            except Exception:
                print("Exception occured creating a DecimalLocation object and appending it to the queue in the"
                      "LocationFactory")
                traceback.print_exc()
        return queue
