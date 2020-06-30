import json

import requests

from main.sample_points_calculator import generate_path_coordinates_list


# This class provides methods to send json requests to the open elevation api server and decode the responses into
# usable elevation data.  This is currently not in use as it is hard to test due to downtime from the open elevation api

# This method takes the coordinates of two Location objects, the number of points to be sampled between them and the
# user's google elevation api key.  These arguments are used to create a valid google elevation api request url of the
# path type.  Returns url as a string.
def construct_url_open_elevation():
    print("Preparing request...")
    api_address = "https://api.open-elevation.com/api/v1/lookup \\"
    return api_address


def construct_json_post_data(location_one, location_two, number_samples):
    # Generate the list of coordinates which form the path between the two locations
    list_of_path_coordinates = generate_path_coordinates_list(location_one, location_two, number_samples)
    # Initialise a list of curly brackets to hold the json code
    data_to_dump = [{}] * len(list_of_path_coordinates)
    # Iterate through the list of coordinates and fill each set of curly brackets with latitude and longitude from the
    # list
    for i in range(len(list_of_path_coordinates)):
        data_to_dump[i] = {"latitude": list_of_path_coordinates[i][0], "longitude": list_of_path_coordinates[i][1]}
    # Wrap the above data in with a final json layer of 'locations'
    location = {"locations": data_to_dump}
    # dump the data into a json object which will be sent to the api
    json_data = json.dumps(location, skipkeys=int).encode('utf8')
    # Return the json object
    return json_data


def send_json_data_to_open_api(location_one, location_two, number_samples):
    # Construct the url
    url = construct_url_open_elevation()
    # Construct the json data to be sent
    json_data = construct_json_post_data(location_one, location_two, number_samples)
    # Create a request object with the url and json data to be sent.  Use post method as the open elevation url post
    # method has no limit to the requests.  Using the normal lookup method has a 1024 byte limit"
    api_response = requests.post(url, json_data)
    return api_response
