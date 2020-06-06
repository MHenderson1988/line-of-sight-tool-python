class Location:
    def __init__(self, a_latitude, a_longitude, a_height, a_name):
        self.latitude = a_latitude
        self.longitude = a_longitude
        self.height = a_height
        self.name = a_name
        self.coordinates = str(self.latitude) + ',' + str(self.longitude)