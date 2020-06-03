import string
import csv

from OSGridConverter import grid2latlong
from pyproj import transform, Proj
from location import Location


# Converts Eastings and Northings to Latitude and Longitude and overwrites .csv file
# Returns a list of Location objects
# To be implemented
def convert_grids_xy(file):
    location_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace='true')
        for row in reader:
            x, y = row[0], row[1]
            in_proj = Proj('epsg:27700')
            out_proj = Proj('epsg:4326')
            x, y = transform(in_proj, out_proj, x, y, always_xy='true')
            lat, long = float(y), float(x)
            height, name = row[2], row[3]
            new_location = Location(lat, long, height, name)
            location_list.append(new_location)

    return location_list


# Turns a standard lat and long .csv file into Location objects
def convert_grids(file):
    location_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', skipinitialspace='true')
        for row in reader:
            lat, long = float(row[0]), float(row[1])
            height, name = float(row[2]), row[3]
            # Create a new Locations objects
            new_location = Location(lat, long, height, name)
            location_list.append(new_location)

    return location_list
