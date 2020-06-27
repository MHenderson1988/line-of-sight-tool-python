# This class calculates the coordinates of the specified amount of points between two locations


# Calculate the interval latitude between the two locations
def calculate_intervals(location_one, location_two):
    interval_latitude = location_two.latitude - location_one.latitude
    interval_longitude = location_two.longitude - location_one.longitude
    return interval_latitude, interval_longitude
