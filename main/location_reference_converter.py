# The location_reference_converter.py class allows for the translation of cartesian references into
# latitude and longitude.

import csv
from pyproj import Transformer

from main.location import Location
from main.validation_handling import validate_longitude_latitude

def process_csv(file):
    type = identify_columns(file)
    if type == 'osbg':
        return convert_easting_northing(file)
    elif type == 'latlong':
        return convert_decimal_lat_long(file)
    else:
        return Exception("Neither OSBG or decimal lat/long detected, please check your csv file.")


# This method reads the .csv file column headings and outputs the correct conversion
def identify_columns(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        for words in header:
            if words == 'Easting':
                print("Easting/Northings detected... Converting...")
                return 'osbg'
            if words == 'Latitude':
                print("Decimal latitude/Longitude detected...")
                return 'latlong'
            else:
                return Exception("Did not detect latitude/longitude, eastings/northings or British National Grid "
                                 "Reference.  Check you have labelled your columns correctly!")


# This converts easting and northing grid references to latitude and longitude.  Creates a Location
# object for each position and returns a list of Location objects.  Currently only tests accurate to 6 decimal degrees

def convert_easting_northing(file) -> list:
    try:
        location_list = []
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile, skipinitialspace=True)
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
            reader = csv.DictReader(csvfile, skipinitialspace=True)
            for row in reader:
                lat, long = float(row['Latitude']), float(row['Longitude'])
                # Validate the input
                validate_longitude_latitude(lat, long)
                height, name = float(row['Height']), row['Name']
                # Create a new Locations objects
                new_location = Location(lat, long, height, name)
                location_list.append(new_location)

        return location_list
    except Exception:
        print("An error occured writing the decimal lat/long")
