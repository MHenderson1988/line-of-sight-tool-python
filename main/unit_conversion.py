# This class converts from one unit into another.  For example it can convert from metres to feet etc.
# This will be used to convert output values to the user's desired unit of measurement.
from typing import Union


# Converts the given argument from metres to feet assuming 1 metre == 3.281 feet
def metres_to_feet(value_in_metres) -> float:
    return value_in_metres * 3.281


# Convert the x_values to the correct unit measurement, as specified by the user
def define_earth_radius(unit_of_distance) -> Union[float, Exception]:
    if unit_of_distance == "NAUTICAL_MILES":
        return 3440.065
    elif unit_of_distance == "MILES":
        return 3958.8
    elif unit_of_distance == "KILOMETRES":
        return 6371.0
    else:
        return Exception("A unit of distance was not specified or there was a type in the gui/code.  Get help!")
