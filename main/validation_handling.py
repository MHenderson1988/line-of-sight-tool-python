# Functions for validating input


# Checks that longitude and latitude are valid decimal form
def validate_longitude_latitude(a_long, a_lat):
    if not isinstance(a_long, float) or not isinstance(a_lat, float):
        raise TypeError("Latitude and longitude must be given in decimal format eg - 55.231, -4.532")
    elif a_long < -180 or a_long > 180:
        raise ValueError("Longitude exceeds it's limits.  Please enter a valid longitude between -180 and 180 degrees")
    elif a_lat < -90 or a_lat > 90:
        raise ValueError("Latitude exceeds it's limits.  Please enter a valid latitude between -90 and 90 degrees")
    else:
        return True


def validate_google_sample_number(a_number):
    if not isinstance(a_number, int):
        raise TypeError("Number of samples must be a whole number greater than 0")
    elif a_number < 1:
        raise ValueError("Number of samples must be a whole number greater than 0")
    else:
        return True
