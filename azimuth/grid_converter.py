import string

from OSGridConverter import grid2latlong
from pyproj import Proj, transform
from reader_writer import *


# Converts Eastings and Northings to Latitude and Longitude and overwrites .csv file
def convert_grids_xy(file):
    my_list = []
    reader = read_csv(file)
    for row in reader:
        in_proj = Proj(init='epsg:27700')
        out_proj = Proj(init='epsg:4326')
        x, y = row[0], row[1]
        x, y = transform(in_proj, out_proj, x, y)
        lat, long = y, x
        height, name = row[2], row[3]
        to_write = lat, long, height, name
        my_list.append(to_write)
        print(to_write)
        write_csv(file, to_write)


# Converts 'Ordinance Survey' grid references into Latitude and Longitude
# If Lat and long are provided, converts to 4 floating points.
def convert_grids(file):
    my_list = []
    # Checks for letters to indicate OS Grid reference
    alpha = string.ascii_letters

    reader = read_csv(file)
    for row in reader:
        if row[0].startswith(tuple(alpha)):
            location = grid2latlong(row[0])
            lat, long = float(location.latitude), float(location.longitude)
            lat, long = format(lat, '4f'), format(long, '4f')
            height, name = row[1], row[2]
        else:
            lat, long = float(row[0]), float(row[1])
            lat, long = format(lat, '4f'), format(long, '4f')
            height, name = row[2], row[3]

        to_write = lat, long, height, name
        my_list.append(to_write)
        print(to_write)

    write_csv(file, to_write)

# For testing
if __name__ == '__main__':
    convert_grids_xy('input_data/grid.csv')