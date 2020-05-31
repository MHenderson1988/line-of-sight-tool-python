import csv
import string

from OSGridConverter import grid2latlong
from pyproj import Proj, transform


def convert_grids_xy(file):
    my_list = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            in_proj = Proj(init='epsg:27700')
            out_proj = Proj(init='epsg:4326')
            x, y = row[0], row[1]
            x, y = transform(in_proj, out_proj, x, y)
            lat = y
            long = x
            height = row[2]
            name = row[3]
            to_write = lat, long, height, name
            my_list.append(to_write)
            print(to_write)

        with open('../inputdata/wind_farms.csv', "w", newline='') as csvfile:
            print("Writing wind_farms.csv: 0%")
            writer = csv.writer(csvfile)
            writer.writerows(my_list)
            print("Writing wind_farms.csv: 100%")


def convert_grids(file):
    my_list = []
    alpha = string.ascii_letters

    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0].startswith(tuple(alpha)):
                location = grid2latlong(row[0])
                lat = float(location.latitude)
                long = float(location.longitude)
                lat = format(lat, '4f')
                long = format(long, '4f')
                height = row[1]
                name = row[2]
            else:
                lat = float(row[0])
                long = float(row[1])
                lat = format(lat, '4f')
                long = format(long, '4f')
                height = row[2]
                name = row[3]

            to_write = lat, long, height, name
            my_list.append(to_write)
            print(to_write)

    with open('../inputdata/wind_farms.csv', "w", newline='') as csvfile:
        print("Writing wind_farms.csv: 0%")
        writer = csv.writer(csvfile)
        writer.writerows(my_list)
        print("Writing wind_farms.csv: 100%")
