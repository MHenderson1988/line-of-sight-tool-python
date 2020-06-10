# This file contains functions which will allow the data to be sent to the elevation API
import json

# This will create the url to be sent to the api
import urllib


def send_and_receive_data(pos_1, pos_2, number_samples, api_key, y_values):
    url = construct_url(pos_1, pos_2, number_samples, api_key)
    sent_request = send_request_google_elevation(url)
    received_data = receive_request_google_elevation(sent_request)
    elevation_data = process_response(received_data, y_values)
    return elevation_data


# This method takes the coordinates of two Location objects, the number of points to be sampled between them and the
# user's google elevation api key.  These arguments are used to create a valid google elevation api request url of the
# path type.  Returns url as a string.
def construct_url(pos_1, pos_2, number_samples, api_key):
    print("Preparing request...")
    api_address = 'https://maps.googleapis.com/maps/api/elevation/json?path='
    url_to_send = api_address + pos_1 + '|' + pos_2 + '&samples=' + str(number_samples) + '&key=' + api_key
    print(url_to_send)
    return url_to_send


# This will send the request to the API.  The url is transformed into a urllib request object with a json data type.
# This request object is then opened using the urlopen command and returns the data from the url as a urlopen object.
def send_request_google_elevation(url):
    print("Sending request...")
    request = urllib.request.Request(url, headers={'Content-Type': 'application/json'})
    urlopen = urllib.request.urlopen(request)
    return urlopen


# This method takes a urlopen object, of json content type, as its argument.  The object is then decoded into utf8
# and returns a decoded string of json data as a string object.
def receive_request_google_elevation(response_from_send_request):
    print("Receiving elevation data...")
    res_byte = response_from_send_request.read()
    res_str = res_byte.decode("utf8")
    js_str = json.loads(res_str)
    response_from_send_request.close()
    return js_str


# This method processes received json data from the google elevation api. The method extracts the 'elevation' values
# and adds the value corresponding to the rise or fall of the pseudo earth ellipsoid created by the Circle class.
# A list of values are returned representing the final elevation values to be processed.
def process_response(return_from_receive_request, earth_surface_values):
    print("Processing and manipulating elevation data...")
    response_len = len(return_from_receive_request['results'])
    elev_list = []
    for j in range(response_len):
        # This manipulates the elevations so that they sit a correct distance above the earth curve
        # In this instance the earth's curve represents the sea-level or '0' in terms of returned elevation values
        elev_list.append(return_from_receive_request['results'][j]['elevation'] + earth_surface_values[j])
    return elev_list
