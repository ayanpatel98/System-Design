from Flight import Flight
from FlightStatus import FlightStatus
import collections

class FlightService:
    
    def __init__(self):
        self.flight_by_src_dest = collections.defaultdict(list[Flight]) # [(src, dest) = [list of flights]]
        self.flight_by_flightNo = collections.defaultdict(Flight) # [flightNumber = flight]
    
    def scheduleFlight(self, flight: Flight):
        if flight.flightNumber in self.flight_by_flightNo:
            print("Flight Already Scheduled")
            return None
        
        self.flight_by_flightNo[flight.flightNumber] = flight
        self.flight_by_src_dest[(flight.src, flight.dest)].append(flight)
        print("flight scheduled")
        return flight
    
    def cancelFlight(self, flightNumber: int):
        if flightNumber not in self.flight_by_flightNo:
            print("flight already unscheduled")
            return False

        flight: Flight = self.flight_by_flightNo[flightNumber]
        flight.flightStatus = FlightStatus.CANCELLED
    
    def searchFlight(self, src: str, dest: str):
        if (src, dest) not in self.flight_by_src_dest:
            print("route not available")
            return None
        
        for flight in self.flight_by_src_dest[(src, dest)]:
            if flight.hasAvailableSeats() and (flight.flightStatus==FlightStatus.ONTIME or flight.flightStatus==FlightStatus.DELAYED):
                return flight
        
        print("flight not available")
        return None


