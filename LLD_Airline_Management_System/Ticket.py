from Flight import Flight
from TicketStatus import TicketStatus

class Ticket:
    def __init__(self, ticketNumber: int, flight: Flight):
        self.ticketNumber = ticketNumber
        self.ticketStatus = TicketStatus.BOOKED
        self.flight = flight
    
    def cancelTicket(self):
        self.flight.cancelSeat()
        self.ticketStatus = TicketStatus.CANCELLED
