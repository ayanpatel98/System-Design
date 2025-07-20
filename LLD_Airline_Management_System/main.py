'''
Airline management system

functional:
- user should be able to search, book / cancel the flight (can be done using a ticket)
- system should be able to add, cancel flights

Entities:
enums: FlightStatus, TicketStatus
Flight: flightNo, FlightStatus, source, destination, capacity, arrival, departure, seats available, has seats, book seat, cancel seat
Ticket: ticketNo, passenger name, flight, cancelTicket()

- User uses
BookingService: tickets, searchFlight(src, dest), bookTicket(flightNumber), cancelTicket(ticketNumber), checkFlightStatus(flightNumber)
- Internally used
FlightService: flight_by_src_dest, flight_by_flightNo, addFlight(flight), cancelFlight(flightNumber), searchFlight(src, dest)


limitations:
    - max people on each flight = flight capacity
'''

from FlightStatus import FlightStatus
from Flight import Flight
from BookingService import BookingService
from FlightService import FlightService

flight1 = Flight(1, FlightStatus.ONTIME, "LAX", "NYC", "2:00PM", "1:00PM", 200)
flight2 = Flight(2, FlightStatus.ONTIME, "LAX", "SJC", "3:00PM", "2:00PM", 200)
flight3 = Flight(3, FlightStatus.ONTIME, "LAX", "EWR", "4:00PM", "3:00PM", 200)

flightService = FlightService()
flightService.scheduleFlight(flight1)
flightService.scheduleFlight(flight2)
flightService.scheduleFlight(flight3)

bookingService = BookingService(flightService)

flightAvailable = bookingService.searchFlights("LAX", "NYC")
ticket = bookingService.bookFlight(flightAvailable.flightNumber)
print(flightAvailable.seatsAvailable)
bookingService.cancelTicket(ticket.ticketNumber)
print(flightAvailable.seatsAvailable)