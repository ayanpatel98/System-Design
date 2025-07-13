'''
- find parking at entrance, if available upon the size then park
- parking has many levels,
- while exit the parking spot is vacated
- Parking manager manages the parking

entities:
- enums, VehicleSize, ParkingSpotStatus
- Vehicle
- ParkingSpot: id, vehicle, Size, ParkingSpotStatus
- Parking Level: list of parking spots, add spots
- Entrance: find parking and Exit gate: vacate parking
- Parking manager: list of levels, add levels, vehicle_parkingSpotMap, find parking, assign parking, vacateParking
'''

from Exit import Exit
from Entrance import Entrance
from ParkingManager import ParkingManager
from Vehicle import Vehicle
from VehicleSize import VehicleSize
from ParkingSpotStatus import ParkingSpotStatus
from Strategy.FindParkingStrategy import FindParkingStrategy

vehicle = Vehicle(1234, VehicleSize.LARGE)

parkingManager = ParkingManager(FindParkingStrategy())
entrance = Entrance(parkingManager)
exit = Exit(parkingManager)

parkingManager.addParkingLevel()
parkingManager.addParkingSpotAtLevel(1, VehicleSize.LARGE)

entrance.assignParkingSpot(entrance.findParkingSport(vehicle), vehicle)
