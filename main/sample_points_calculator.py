# This class calculates the coordinates of the specified amount of points between two locations


# Calculate the interval latitude between the two locations
def calculate_intervals(location_one, location_two, amount_of_samples):
    interval_latitude = (location_two.latitude - location_one.latitude) / amount_of_samples
    interval_longitude = (location_two.longitude - location_one.longitude) / amount_of_samples
    return interval_latitude, interval_longitude
