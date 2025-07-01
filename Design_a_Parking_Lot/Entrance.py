from models.Vehicle import Vehicle
from models.VehicleType import VehicleType
from ParkingManagerTwoWheeler import ParkingManagerTwoWheeler
from ParkingManagerFourWheeler import ParkingManagerFourWheeler
from Ticket import Ticket
from ParkingManagerFactory import ParkingManagerFactory

class Entrance:
    def __init__(self):
        self.parkingManagerFactory = ParkingManagerFactory()
    
    def findParkingSpot(self, vehicle: Vehicle):
        parkingManager = self.parkingManagerFactory.getParkingManager(vehicle)
        
        return parkingManager.findParkingSpot()
    
    def parkVehicle(self, vehicle: Vehicle, spot):
        parkingManager = self.parkingManagerFactory.getParkingManager(vehicle)
        
        parkingManager.parkVehicle(vehicle, spot)
    
    def generateTicket(self, vehicle: Vehicle, spot):
        ticket = Ticket(spot, vehicle)
        return ticket
    
    def getParkingManager(self, vehicle):
        return self.parkingManagerFactory.getParkingManager(vehicle)
        

        