from FlightService import FlightService
from Ticket import Ticket
from Flight import Flight
from TicketStatus import TicketStatus

class BookingService:

    def __init__(self, flightService: FlightService):
        self.flightService = flightService
        self.tickets = {}
    
    def searchFlights(self, src: str, dest: str):
        return self.flightService.searchFlight(src, dest)
    
    def bookFlight(self, flightNumber: int):
        if flightNumber not in self.flightService.flight_by_flightNo:
            print("invalid flight number")
            return None
        
        flight: Flight = self.flightService.flight_by_flightNo[flightNumber]

        flight.bookSeat()
        ticket = Ticket(len(self.tickets)+1, flight)
        self.tickets[ticket.ticketNumber] = ticket
        print("Flight Booked")
        return ticket
    
    def cancelTicket(self, ticketNumber: int):
        if ticketNumber not in self.tickets:
            print("Ticket not available")
            return False
        
        ticket: Ticket = self.tickets[ticketNumber]
        flight: Flight = ticket.flight
        flight.cancelSeat()
        ticket.ticketStatus = TicketStatus.CANCELLED
        print("ticket cancelled")
        return True
    
    def checkFlightStatus(self, flightNumber: int):
        if flightNumber not in self.flightService.flight_by_flightNo:
            print("invalid flight number")
            return None
        
        flight: Flight = self.flightService.flight_by_flightNo[flightNumber]
        return flight.flightStatus
        


