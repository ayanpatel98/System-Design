from models.Vehicle import Vehicle
from abc import ABC, abstractmethod

class ParkingSpot:

    def __init__(self, id):
        self.id = id
        self.vehicle = None
        self.isEmpty = True

    def parkVehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.isEmpty = False

    def removeVehicle(self):
        self.vehicle = None
        self.isEmpty = True
    
    @abstractmethod
    def price(self):
        pass