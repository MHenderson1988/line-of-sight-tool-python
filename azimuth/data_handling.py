# This file contains functions which will allow the data to be sent to the elevation API
import urllib.request
import json


# This will send the request to the API
def send_request_google_elevation(pos_1, pos_2, number_samples, api_key):
    print("Sending request...")
    url = construct_url(pos_1, pos_2, api_key, number_samples)
    response = urllib.request.Request(url, headers={'Content-Type': 'application/json'})
    fp = urllib.request.urlopen(response)
    return fp


# This will create the url to be sent to the api
def construct_url(pos_1, pos_2, number_samples, api_key):
    print("Preparing request...")
    api_address = 'https://maps.googleapis.com/maps/api/elevation/json?path='
    print(api_address)
    return api_address + pos_1 + '|' + pos_2 + '&samples=' + str(number_samples) + '&key=' + api_key


# This will receive data from the google elevation API
def receive_request_google_elevation(response_from_send_request):
    print("Receiving elevation data...")
    res_byte = response_from_send_request.read()
    res_str = res_byte.decode("utf8")
    js_str = json.loads(res_str)
    response_from_send_request.close()
    return js_str


# This will retrieve the elevation from the response
# Returns a list of elevations between the two points.
def process_response(return_from_receive_request, earth_surface_values):
    print("Processing and manipulating elevation data...")
    response_len = len(return_from_receive_request['results'])
    elev_list = []
    for j in range(response_len):
        # This manipulates the elevations so that they sit a correct distance above the earth curve
        # In this instance the earth's curve represents the sea-level or '0' in terms of returned elevation values
        elev_list.append(return_from_receive_request['results'][j]['elevation'] + earth_surface_values[j])
    return elev_list
