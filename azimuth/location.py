class Locations:
    def __init__(self, a_latitude, a_longitude, a_height, a_name):
        self.latitude = a_latitude
        self.longitude = a_longitude
        self.height = a_height
        self.name = a_name
        self.coordinates = str(self.latitude) + ',' + str(self.longitude)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, a_latitude):
        self._latitude = a_latitude

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, a_longitude):
        self._longitude = a_longitude

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, a_height):
        self._height = a_height

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a_name):
        self._name = a_name
