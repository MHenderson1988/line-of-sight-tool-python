import json
import urllib.request


class GoogleHandler:
    def __init__(self, *args, **kwargs):
        self.loc1 = args[0]
        self.loc2 = args[1]
        self.samples = kwargs.get('samples', 150)
        self.api_key = kwargs.get('key', "NULL")
        self.distance_units = kwargs.get('distance_units', 'NAUTICAL_MILES')
        self.height_units = kwargs.get('height_units', 'FEET')
        self.base_url = 'https://maps.googleapis.com/maps/api/elevation/json?path='
        self.request_url = self.base_url + str(self.loc1.y) + ',' + str(self.loc1.x) + '|' + str(self.loc2.y) + \
                           ',' + str(self.loc2.x) + '&samples=' + str(self.samples) + '&key=' + self.api_key
        self.elevation_data = self.process()

    def process(self):
        return self.process_response()

    # This will send the request to the API.  The url is transformed into a urllib request object with a json data
    # type. This request object is then opened using the urlopen command and returns the data from the url as a
    # urlopen object.

    def send_request(self):
        request = urllib.request.Request(self.request_url, headers={'Content-Type': 'application/json'})
        return urllib.request.urlopen(request)

    # This method takes a urlopen object, of json content type, as its argument.  The object is then decoded into utf8
    # and returns a decoded string of json data as a string object.
    def receive_request(self):
        res_byte = self.send_request().read()
        res_str = res_byte.decode("utf8")
        js_str = json.loads(res_str)
        self.send_request().close()
        return js_str

    # This method processes received json data from the google elevation api. The method extracts the 'elevation' values
    # and adds the value corresponding to the rise or fall of the pseudo earth ellipsoid created by the Circle class.
    # A list of values are returned representing the final elevation values to be processed.
    def process_response(self):
        request = self.receive_request()
        list = []
        response_len = len(request['results'])
        for j in range(response_len):
            # This manipulates the elevations so that they sit a correct distance above the earth curve
            # In this instance the earth's curve represents the sea-level or '0' in terms of returned elevation values
            # Google api returns in metres so we must convert to feet if that is the height unit specified
            if self.height_units == "METRES":
                list.append(request['results'][j]['elevation'])
            if self.height_units == "FEET":
                list.append(request['results'][j]['elevation'] * 3.281)

        return list

    def __str__(self):
        return "Google Handler object for querying the Google Elevation API between {self.loc1}" \
               " and {self.loc2}".format(self=self)
