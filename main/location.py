class Location:
    def __init__(self, a_latitude, a_longitude, a_height, a_name):
        self.latitude = a_latitude
        self.longitude = a_longitude
        self.height = a_height
        self.name = a_name
        # This is used for the kml generator which takes long lat not lat long
        self.coordinates = self.longitude, self.latitude, self.height
        self.coordinates_string = str(self.latitude) + ',' + str(self.longitude)
