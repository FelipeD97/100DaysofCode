class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, cityFrom, cityTo, nightsInDest, price):
        self.price = price
        self.cityFrom = cityFrom
        self.cityTo = cityTo
        self.nightsInDest = nightsInDest
