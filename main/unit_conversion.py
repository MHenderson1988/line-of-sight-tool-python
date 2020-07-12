# This class converts from one unit into another.  For example it can convert from metres to feet etc.
# This will be used to convert output values to the user's desired unit of measurement.


# Converts the given argument from metres to feet assuming 1 metre == 3.281 feet
def metres_to_feet(value_in_metres):
    return value_in_metres * 3.281


# Converts the given argument from nautical miles to metres assuming 1 nautical mile == 1852 feet.
def nautical_miles_to_metres(value_in_nautical_miles):
    return value_in_nautical_miles * 1852


# Converts the given argument from nautical miles to feet, assuming 1 nautical miles == 6076 feet.
def nautical_miles_to_feet(value_in_nautical_miles):
    return value_in_nautical_miles * 6076


# Converts the given argument from nautical miles to statute miles assuming 1 nautical mile == 1.151 statute miles
def nautical_miles_to_statute_miles(value_in_nautical_miles):
    return value_in_nautical_miles * 1.151


# Converts the given argument from nautical miles to kilometres assuming 1 nautical mile == 1.852 kilometres
def nautical_miles_to_kilometres(value_in_nautical_miles):
    return value_in_nautical_miles * 1.852


# Convert the x_values to the correct unit measurement, as specified by the user
def convert_distance_measurement(list_of_x_values, distance_units):
    if distance_units == "Nautical miles(Nm)":
        return list_of_x_values
    elif distance_units == "Miles(Mi)":
        for i in list_of_x_values:
            list_of_x_values[i] = nautical_miles_to_statute_miles(list_of_x_values[i])
    elif distance_units == "Kilometres(Km)":
        for i in list_of_x_values:
            list_of_x_values[i] = nautical_miles_to_kilometres(list_of_x_values[i])
    else:
        return Exception("No distance units selected, you broke it somehow!!!!")
