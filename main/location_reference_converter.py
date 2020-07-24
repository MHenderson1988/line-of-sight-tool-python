# The location_reference_converter.py class allows for the translation of cartesian references into
# latitude and longitude.

import csv
from typing import Union

import OSGridConverter
from pyproj import Transformer

from main.location import Location
from main.validation_handling import validate_longitude_latitude


# This method verifies which conversion method to call.  Returns a list of Location objects in decimal lat-long format.

def conversion_type(file, coordinate_type) -> Union[list, int]:
    if coordinate_type == "decimal":
        list_to_return = convert_decimal_lat_long(file)
        return list_to_return
    elif coordinate_type == "xy":
        list_to_return = convert_easting_northing(file)
        return list_to_return
    elif coordinate_type == "bng":
        list_to_return = convert_british_national_grid(file)
        return list_to_return
    else:
        return 0


# This converts easting and northing grid references to latitude and longitude.  Creates a Location
# object for each position and returns a list of Location objects.  Currently only tests accurate to 6 decimal degrees

def convert_easting_northing(file) -> list:
    try:
        location_list = []
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', skipinitialspace='true')
            for row in reader:
                try:
                    transformer = Transformer.from_crs('epsg:27700', 'epsg:4326')
                    x, y = transformer.transform(row[0], row[1])
                    location = Location(round(x, 6), round(y, 6), row[2], row[3])
                    location_list.append(location)
                except Exception:
                    print("Exceptions at row converting xy to decimal lat/long")
        return location_list
    except Exception:
        print("An error occured converting eastings and northings to decimal lat/long")


# This is what the google elevation api accepts.  Therefore a decimal lat long will simply be written to a new
# Location class object and WILL NOT undergo any conversion.
# Returns a list of Location objects

def convert_decimal_lat_long(file) -> list:
    try:
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
    except Exception:
        print("An error occured writing the decimal lat/long")


# This function takes an Ordinance Survey National Grid Reference (British National Grid) and converts it to a
# decimal lat and long.  This conversion is then used to make a new Location object which is added to a list.
# A list of Location objects is returned.  This currently only passes tests to 4 decimal places / 11.1m.

def convert_british_national_grid(file) -> list:
    try:
        location_list = []
        with open(file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', skipinitialspace='true')
            for row in reader:
                grid_converter = OSGridConverter.grid2latlong(row[0])
                latitude = grid_converter.latitude
                longitude = grid_converter.longitude
                height, name = float(row[1]), row[2]
                new_location = Location(latitude, longitude, height, name)
                location_list.append(new_location)
        return location_list
    except Exception:
        print("An error occured converting BNG to decimal latitude/longitude")
