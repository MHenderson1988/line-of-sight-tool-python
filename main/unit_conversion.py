# Discovers the value of user input for units of height or distance
def get_user_selected_unit_and_convert(value_to_convert, unit_of_measurement):
    if unit_of_measurement == 'Nautical miles':
        return value_to_convert
    elif unit_of_measurement == 'Km':
        return convert_nm_to_km(value_to_convert)
    elif unit_of_measurement == 'Miles':
        return convert_nm_to_miles(value_to_convert)
    elif unit_of_measurement == 'Feet':
        return convert_nm_to_feet(value_to_convert)
    elif unit_of_measurement == 'Meters':
        return convert_nm_to_meters(value_to_convert)
    else:
        return "Error, please select a valid unit of output"


# This converts a nautical mile value to meters
def convert_nm_to_meters(nm_value):
    return nm_value * 1852


# This converts a nautical mile value to kilometers
def convert_nm_to_km(nm_value):
    return nm_value * 1.852


# Returns a converted nautical mile value to statute miles
def convert_nm_to_miles(nm_value):
    return nm_value * 1.15078


# Returns a nautical mile value converted to feet
def convert_nm_to_feet(nm_values):
    return nm_values * 6076.12
