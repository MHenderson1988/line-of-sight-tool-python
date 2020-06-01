class Locations:
    def __init__(self, a_latitude, a_longitude, a_height, a_name):
        self.latitude = a_latitude
        self.longitude = a_longitude
        self.height = a_height
        self.name = a_name

    def set_latitude(self, a_latitude):
        self.latitude = a_latitude

    def set_longitude(self, a_longitude):
        self.longitude = a_longitude

    def set_height(self, a_height):
        self.height = a_height

    def set_name(self, a_name):
        self.name = a_name
