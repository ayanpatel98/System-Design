from ParkingSpot import ParkingSpot

class TwoWheelerParkingSpot(ParkingSpot):
    _price = 10

    def price(self):
        return TwoWheelerParkingSpot._price
    