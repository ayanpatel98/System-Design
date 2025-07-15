from FlightStatus import FlightStatus

class Flight:

    def __init__(self, flightNumber: int, flightStatus: FlightStatus, src: str, dest: str, arrival, departure, capacity: int):
        self.flightNumber = flightNumber
        self.flightStatus = flightStatus
        self.src = src
        self.dest = dest
        self.arrival = arrival
        self.departure = departure
        self.capacity = capacity
        self.seatsAvailable = self.capacity
    
    def hasAvailableSeats(self):
        return self.seatsAvailable>0
    
    def cancelSeat(self):
        if self.seatsAvailable<=self.capacity:
            self.seatsAvailable+=1
    
    def bookSeat(self):
        if self.seatsAvailable>=0:
            self.seatsAvailable-=1