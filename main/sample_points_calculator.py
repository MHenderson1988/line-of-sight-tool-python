# This class calculates the coordinates of the specified amount of points between two locations
# These coordinates will be used to interrogate the Open elevation API, which does not currently have a
# path feature like Google Elevation.


# Calculate the interval latitude between the two locations.
# Takes two Location objects as arguments and returns two floating point numbers, one for latitude and one for longitude
def calculate_intervals(location_one, location_two, amount_of_samples) -> tuple:
    # Calculate the longitude and latitude interval by finding the difference between the end and the starting location
    # values and then dividing by the amount of samples specified by the user
    try:
        interval_latitude = (location_two.latitude - location_one.latitude) / amount_of_samples
        interval_longitude = (location_two.longitude - location_one.longitude) / amount_of_samples

        # Return the latitude and longitude interval and end the method
        return interval_latitude, interval_longitude
    except Exception:
        print("An error occured whilst calculating the intervals")


# Generate a path of coordinates between the first and second locations.
# Arguments - two location objects and returns a list of coordinates.  The first being the starting coordinates and the
# last is the ending coordinates.
def generate_path_coordinates_list(location_one, location_two, amount_of_samples) -> list:
    try:
        # Set the starting coordinates
        start_coordinates = location_one.coordinates_lat_long
        # Add the starting coordinates to the list to be iterated over.
        path_list = [start_coordinates]
        # Calculate the interval to be added each pass, by calling the calculate_intervals function
        latitude_interval, longitude_interval = calculate_intervals(location_one, location_two, amount_of_samples)

        # For the amount of samples required, add the interval latitude and longitude to the current coordinates.  And
        # add those coordinates to the list to be returned which will then be iterated over again in the next pass.
        for i in range(amount_of_samples):
            current_latitude, current_longitude = path_list[i][0], path_list[i][1]
            new_latitude, new_longitude = round(current_latitude + latitude_interval, 7), round(
                current_longitude + longitude_interval, 7)
            path_list.append((new_latitude, new_longitude))

        # Return the list of coordinates which make up the path between the locations and end the method
        return path_list
    except Exception:
        print("An error occured generating the path coordinates")
