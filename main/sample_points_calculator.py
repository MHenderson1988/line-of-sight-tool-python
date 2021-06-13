# Generate a path of coordinates between the first and second locations.
# Arguments - two classes objects and returns a list of coordinates.  The first being the starting coordinates and the
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
