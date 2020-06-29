import json

from main.sample_points_calculator import generate_path_coordinates_list


# This method takes the coordinates of two Location objects, the number of points to be sampled between them and the
# user's google elevation api key.  These arguments are used to create a valid google elevation api request url of the
# path type.  Returns url as a string.
def construct_url_open_elevation(location_one, location_two, number_samples):
    print("Preparing request...")
    api_address = "https://api.open-elevation.com/api/v1/lookup \\"


def construct_json_post_data(location_one, location_two, number_samples):
    list_of_path_coordinates = generate_path_coordinates_list(location_one, location_two, number_samples)
    data_to_dump = [{}] * len(list_of_path_coordinates)

    for i in range(len(list_of_path_coordinates)):
        data_to_dump = {"latitude": list_of_path_coordinates[i][0], "longitude": list_of_path_coordinates[i][1]}
    location = {"locations": data_to_dump}
    json_data = json.dumps(location, skipkeys=int).encode('utf8')
