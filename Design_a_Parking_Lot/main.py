from models.Vehicle import Vehicle
from models.VehicleType import VehicleType
from Entrance import Entrance
from Exit import Exit

if __name__=="__main__":
    vehicle = Vehicle("GJ-01", VehicleType.TWO_WHEELER)
    entrance = Entrance()
    
    spot = entrance.findParkingSpot(vehicle)
    entrance.parkVehicle(vehicle, spot)
    ticket = entrance.generateTicket(vehicle, spot)
    print(spot.id)

    exit = Exit()
    exit.calculatePrice(ticket)

    
    # For checking if the parking manager maintains a central list of parking spots as it is singleton
    # vehicle = Vehicle("GJ-01", VehicleType.TWO_WHEELER)
    # entrance1 = Entrance()
    # entrance2 = Entrance()

    # manager1 = entrance1.getParkingManager(vehicle)
    # manager1.addSpot()
    # print(len(manager1.parkingSpotList))
    

    # manager2 = entrance2.getParkingManager(vehicle)
    # manager2.deleteSpot()
    # manager2.deleteSpot()
    # print(len(manager2.parkingSpotList))
    