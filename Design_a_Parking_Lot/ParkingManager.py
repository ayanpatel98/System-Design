from models.Vehicle import Vehicle
from ParkingSpot import ParkingSpot
from models.VehicleType import VehicleType
from TwoWheelParkingSpot import TwoWheelerParkingSpot
from FourWheelParkingSpot import FourWheelerParkingSpot

class ParkingManager:
    def __init__(self, list: list[ParkingSpot]):
        self.parkingSpotList = list
        self.parkingSpot = None
    
    def findParkingSpot(self):
        for parkingSpot in self.parkingSpotList:
            if parkingSpot.isEmpty:
                return parkingSpot
        return None

    def parkVehicle(self, vehicle: Vehicle, parkingSpot: ParkingSpot):
        if parkingSpot:
            parkingSpot.parkVehicle(vehicle)
            print("Vehicle Parked")
        else:
            print("Error While parking")

    def removeVehicle(self, parkingSpot: ParkingSpot):
        if parkingSpot:
            parkingSpot.removeVehicle()
            print("Vehicle Removed")
        else:
            print("Error While Removing")
    
    def deleteSpot(self):
        self.parkingSpotList.pop()

    def addSpot(self, vehicleType: VehicleType):
        if vehicleType==VehicleType.TWO_WHEELER:
            self.parkingSpotList.append(TwoWheelerParkingSpot(len(self.parkingSpotList)-1))
        else:
            self.parkingSpotList.append(FourWheelerParkingSpot(len(self.parkingSpotList)-1))
     