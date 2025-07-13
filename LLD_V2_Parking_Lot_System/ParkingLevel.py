from ParkingSpot import ParkingSpot
from ParkingSpotStatus import ParkingSpotStatus
from VehicleSize import VehicleSize
from Vehicle import Vehicle

class ParkingLevel:

    def __init__(self):
        self.parkingSpotList: list[ParkingSpot] = []
    
    def addParkingSpot(self, size: VehicleSize):
        self.parkingSpotList.append(ParkingSpot(len(self.parkingSpotList)+1, size))
        print("Parking Spot added")