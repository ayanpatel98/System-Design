from Vehicle import Vehicle
from ParkingManager import ParkingManager
from typing import Optional
from ParkingSpot import ParkingSpot

class Entrance:
    def __init__(self, parkingManager: ParkingManager):
        self.parkingManager = parkingManager

    def findParkingSpot(self, vehicle: Vehicle)->Optional[ParkingSpot]:
        return self.parkingManager.findParkingSpot(vehicle)
    
    def assignParkingSpot(self, parkingSpot: ParkingSpot, vehicle: Vehicle):
        self.parkingManager.assignParkingSpot(parkingSpot, vehicle)