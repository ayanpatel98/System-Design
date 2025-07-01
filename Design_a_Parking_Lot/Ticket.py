from models.Vehicle import Vehicle
from ParkingSpot import ParkingSpot

class Ticket:
    def __init__(self, parkingSpot: ParkingSpot, vehicle: Vehicle):
        self.parkingSpot = parkingSpot
        self.vehicle = vehicle
    
    def getTicket():
        return self