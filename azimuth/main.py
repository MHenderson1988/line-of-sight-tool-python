import grid_converter
import line_of_sight_calculations
import data_processing
import kml_generator
import locations
import circle

from haversine import haversine, Unit

# Create a list of location objects from both .csv files
# File one
first_location_list = grid_converter.convert_grids_xy('../inputdata/grid.csv')

# File two
second_location_list = grid_converter.convert_grids('../inputdata/radars.csv')

# Calculate great circle distance between points
# To add functionaility for difference units of measurement
for i in first_location_list:
    pos_1 = (i.latitude, i.longitude)
    for x in second_location_list:
        pos_2 = (x.latitude, x.longitude)
        print(pos_1, pos_2)
        print(haversine(pos_1, pos_2, unit=Unit.NAUTICAL_MILES))

