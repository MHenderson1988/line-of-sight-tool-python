# The location_reference_converter.py class allows for the translation of cartesian references into
# latitude and longitude.

import csv
from typing import Union

import OSGridConverter
from pyproj import Transformer

from main.location import Location
from main.validation_handling import validate_longitude_latitude

# This method reads the .csv file column headings and outputs the correct conversion
# TODO - Alter other methods to work with new identify_columns method
def identify_columns(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        for words in header:
            if words == 'Easting' or words == 'easting':
                print("Easting/Northings detected... Converting...")
                return convert_easting_northing(reader)
            if words == 'Latitude' or words == 'latitude':
                print("Decimal latitude/Longitude detected...")
                return convert_decimal_lat_long(reader)
            if words == 'Grid' or words == 'grid':
                print("British national grid detected... Converting...")
                return 'bng'
            else:
                return Exception("Did not detect latitude/longitude, eastings/northings or British National Grid "
                                 "Reference.  Check you have labelled your columns correctly!")


# This converts easting and northing grid references to latitude and longitude.  Creates a Location
# object for each position and returns a list of Location objects.  Currently only tests accurate to 6 decimal degrees

def convert_easting_northing(reader) -> list:
    try:
        location_list = []
        for row in reader:
            try:
                transformer = Transformer.from_crs('epsg:27700', 'epsg:4326')
                x, y = transformer.transform(row['Easting'], row['Northing'])
                location = Location(round(x, 6), round(y, 6), row['Height'], row['Name'])
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
            reader = csv.DictReader(csvfile)
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
            reader = csv.DictReader(csvfile)
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
