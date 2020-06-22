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
