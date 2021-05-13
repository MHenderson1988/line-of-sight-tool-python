# This class converts from one unit into another.  For example it can convert from metres to feet etc.
# This will be used to convert output values to the user's desired unit of measurement.
from typing import Union

from haversine import haversine, Unit


# Converts the given argument from metres to feet assuming 1 metre == 3.281 feet
def metres_to_feet(value_in_metres) -> float:
    return value_in_metres * 3.281


# Convert the x_values to the correct unit measurement, as specified by the user
def define_earth_radius(unit_of_distance) -> Union[float, Exception]:
    if unit_of_distance == "Nautical miles":
        return 3440.065
    elif unit_of_distance == "Miles":
        return 3958.8
    elif unit_of_distance == "Kilometres":
        return 6371.0
    else:
        return Exception("A unit of distance was not specified or there was a type in the gui/code.  Get help!")


# Returns the great circle distance in the correct units of measurement, depending on what the user specified on the GUI
# Takes arguments of units of distance and two positions with long/lat
def calculate_great_circle_distance(pos_1, pos_2, unit_of_distance):
    if unit_of_distance == "Nautical miles":
        return haversine(pos_1, pos_2, unit=Unit.NAUTICAL_MILES)
    elif unit_of_distance == "Miles":
        return haversine(pos_1, pos_2, unit=Unit.MILES)
    elif unit_of_distance == "Kilometres":
        return haversine(pos_1, pos_2, unit=Unit.KILOMETERS)
    else:
        return Exception("A unit of distance was not specified or there was a type in the gui/code.  Get help!")


# Returns a converted height value based upon the distance and height units of measurement selected by the user
def convert_y_values(y_value, distance_units, height_units) -> Union[float, Exception]:
    if distance_units == "Nautical miles":
        if height_units == "Feet":
            return y_value * 6076
        if height_units == "Metres":
            return y_value * 1852
        else:
            return Exception("Something went wrong converting nautical miles to the selected height units")
    elif distance_units == "Kilometres":
        if height_units == "Feet":
            return y_value * 3281
        if height_units == "Metres":
            return y_value * 1000
        else:
            return Exception("Something went wrong converting Kilometres to the selected height units")
    elif distance_units == "Miles":
        if height_units == "Feet":
            return y_value * 5280
        if height_units == "Metres":
            return y_value * 1609.34
    else:
        return Exception("Something went wrong converting y values from the distance units to the height units.")
