from Vehicle import Vehicle
from ParkingManager import ParkingManager
from typing import Optional
from ParkingSpot import ParkingSpot

class Exit:
    def __init__(self, parkingManager: ParkingManager):
        self.parkingManager = parkingManager

    def exitParking(self, vehicle: Vehicle):
        self.parkingManager.exitParking(vehicle)