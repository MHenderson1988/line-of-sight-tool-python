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
