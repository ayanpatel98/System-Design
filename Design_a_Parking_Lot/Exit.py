from Ticket import Ticket
from TwoWheelParkingSpot import TwoWheelerParkingSpot
from FourWheelParkingSpot import FourWheelerParkingSpot

class Exit:
    def __init__(self):
        self.ticket = None
    
    def calculatePrice(self, ticket: Ticket):
        
        print(ticket.parkingSpot.price())