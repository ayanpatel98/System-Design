'''
Airline manegment system

functional:
- user should be able to book / cancel the flight (can be done using a ticket)
- system should be able to add or cancel flights

Entities:
enums: FlightStatus, TicketStatus
Flight: flightNo, FlightStatus, source, destination, capacity, arrival, departure, seats available, has seats, book seat, cancel seat
Ticket: ticketNo, flight

- User uses
BookingService: searchFlight(src, dest), bookTicket(flightNumber), cancelTicket(ticketNumber), checkFlightStatus(ticketNumber)
- Internally used
FlightService: addFlight(src, dest), cancelFlight(flightNumber), searchFlight(src, dest)


limitations:
    - max people on each flight = flight capacity
'''