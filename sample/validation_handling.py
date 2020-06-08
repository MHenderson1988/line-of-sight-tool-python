# Functions for validating input


# Checks that longitude and latitude (WGS83) are valid.
def validate_longitude_latitude(a_long, a_lat):
    if a_long < -180 or a_long > 180:
        raise ValueError("Longitude exceeds it's limits.  Please enter a valid longitude between -180 and 180 degrees")
    if a_lat < -90 or a_lat > 90:
        raise ValueError("Latitude exceeds it's limits.  Please enter a valid latitude between -90 and 90 degrees")
    if a_long or a_lat != type(float):
        raise TypeError("Latitude and longitude must be given in decimal format eg - 55.231, -4.532")