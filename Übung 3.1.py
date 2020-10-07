class WGS84Coord:
    def __init__(self, longitude=0, latitude=0):
        self._setLongitude(longitude)
        self._setLatitude(latitude)

    def _setLongitude(self, longitude):
        self._longitude = longitude
        while self._longitude < -180:
            self._longitude = 180 + (self._longitude + 180)
            print("Value not in range! New Value:" + str(self._longitude))
        while self._longitude > 180:
            self._longitude = -180 + (self._longitude - 180)
            print("Value not in range! New Value:" + str(self._longitude))

    def _setLatitude(self, latitude):
        self._latitude = latitude
        while self._latitude < -90:
            self._latitude = -90 - (self._latitude + 90)
            print("Value not in range! New Value:" + str(self._latitude))
        while self._latitude > 90:
            self._latitude = + 90 - (self._latitude - 90)
            print("Value not in range! New Value:" + str(self._latitude))

    def _getLongitude(self):
        return self._longitude
    def _getLatitude(self):
        return self._latitude
    def __str__(self):
        return "Point (" + str(self._longitude) + " " + str(self._latitude) + ")"

    latitude = property(_getLongitude, _setLongitude)
    longitude = property(_getLongitude, _setLongitude)

Koord = WGS84Coord(34, 23)
print(Koord)

