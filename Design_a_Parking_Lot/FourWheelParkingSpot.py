from ParkingSpot import ParkingSpot

class FourWheelerParkingSpot(ParkingSpot):
    _price = 20

    def price(self):
        return FourWheelerParkingSpot._price
    