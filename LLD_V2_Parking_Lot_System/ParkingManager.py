from ParkingLevel import ParkingLevel
from Vehicle import Vehicle
from ParkingSpot import ParkingSpot
from VehicleSize import VehicleSize
from ParkingSpotStatus import ParkingSpotStatus
from Strategy.Strategy import Strategy

class ParkingManager:
    _instance = None
    
    def __new__(cls, findingStrategy: Strategy):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, findingStrategy: Strategy):
        if not hasattr(self, "_initialized"):
            self.parkingLevels: list[ParkingLevel] = []
            self.parkingSpotLog = {}
            self.findingStrategy = findingStrategy
    
    def addParkingLevel(self):
        self.parkingLevels.append(ParkingLevel())
        print("Parking Level Added")
    
    def addParkingSpotAtLevel(self, level: int, size: VehicleSize):
        if level > len(self.parkingLevels) or level<=0:
            print("Invalid Level")
            return
        self.parkingLevels[level-1].addParkingSpot(size)
        print("Level Added")
    
    def findParkingSpot(self, vehicle: Vehicle):
        for level in self.parkingLevels:
            parkingSpot = self.findingStrategy.findParkingSpot(level, vehicle)
            if parkingSpot:
                return parkingSpot
            print("No Parking Spot Available")
            
    def assignParkingSpot(self, parkingSpot: ParkingSpot, vehicle: Vehicle):
        parkingSpot.status = ParkingSpotStatus.NOT_AVAILABLE
        parkingSpot.vehicle = vehicle
        self.parkingSpotLog[vehicle.number] = parkingSpot
        print("Parking Assigned at: ", parkingSpot.id)

    def exitParking(self, vehicle: Vehicle):
        if vehicle not in self.parkingSpotLog:
            print("vehicle Already exited")
            return
        
        parkingSpot: ParkingSpot = self.parkingSpotLog[vehicle]
        parkingSpot.status = ParkingSpotStatus.AVAILABLE
        parkingSpot.vehicle = None
        print("Vehicle Exited")
        