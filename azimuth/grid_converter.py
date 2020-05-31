import string
import csv

from OSGridConverter import grid2latlong
from pyproj import Proj, transform
from locations import Locations


# Converts Eastings and Northings to Latitude and Longitude and overwrites .csv file
# Returns a list of Location objects
def convert_grids_xy(file):
    location_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            in_proj, out_proj = Proj(init='epsg:27700'), Proj(init='epsg:4326')
            x, y = row[0], row[1]
            x, y = transform(in_proj, out_proj, x, y)
            lat, long = y, x
            height, name = row[2], row[3]
            new_location = Locations(lat, long, height, name)
            location_list.append(new_location)

    print(location_list)

    return location_list


def convert_grids(file):
    location_list = []
    alpha = string.ascii_letters

    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0].startswith(tuple(alpha)):
                location = grid2latlong(row[0])
                lat = float(location.latitude), float(location.longitude)
                lat, long = format(lat, '4f'), format(long, '4f')
                height, name = row[1], row[2]
            else:
                lat, long = float(row[0]), float(row[1])
                lat, long = format(lat, '4f'), format(long, '4f')
                height, name = row[2], row[3]
            # Create a new Locations objects
            new_location = Locations(lat, long, height, name)
            location_list.append(new_location)

    return location_list


# For testing
if __name__ == '__main__':
    convert_grids_xy('..\inputdata\grid.csv')
