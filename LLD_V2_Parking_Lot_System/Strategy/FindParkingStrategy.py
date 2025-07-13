from Strategy.Strategy import Strategy
from ParkingLevel import ParkingLevel
from Vehicle import Vehicle
from ParkingSpotStatus import ParkingSpotStatus

class FindParkingStrategy(Strategy):

    def findParkingSpot(self, level: ParkingLevel, vehicle: Vehicle):
        for parkingSpot in sorted(level.parkingSpotList, key = lambda x: x.size.value):
            if parkingSpot.status==ParkingSpotStatus.AVAILABLE and parkingSpot.size.value>=vehicle.vehicleSize.value:
                return parkingSpot
        return None