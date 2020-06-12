# The location_reference_converter.py class allows for the translation of cartesian references into
# latitude and longitude.

import csv

from pyproj import Transformer

from main.location import Location
from main.validation_handling import validate_longitude_latitude


def convert_easting_northing(file):
    location_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace='true')
        for row in reader:
            transformer = Transformer.from_crs('epsg:27700', 'epsg:4326')
            x, y = transformer.transform(row[0], row[1])
            location = Location(x, y, row[2], row[3])
            location_list.append(location)
    return location_list


# This is what the google elevation api accepts.  Therefore a decimal lat long will simply be written to a new
# Location class object and WILL NOT undergo any conversion.
# Returns a list of Location objects
def convert_decimal_lat_long(file):
    location_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace='true')
        for row in reader:
            lat, long = float(row[0]), float(row[1])
            # Validate the input
            validate_longitude_latitude(lat, long)
            height, name = float(row[2]), row[3]
            # Create a new Locations objects
            new_location = Location(lat, long, height, name)
            location_list.append(new_location)

    return location_list
