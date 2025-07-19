from VehicleSize import VehicleSize
from ParkingSpotStatus import ParkingSpotStatus
from Vehicle import Vehicle

class ParkingSpot:

    def __init__(self, id: int, size: VehicleSize):
        self.id = id
        self.vehicle = None
        self.size = size
        self.status = ParkingSpotStatus.AVAILABLE
    
    def setParkingSpotStatus(self, status: ParkingSpotStatus):
        self.status = status

    def setParkingSpotVehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle

