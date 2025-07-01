from ParkingManagerTwoWheeler import ParkingManagerTwoWheeler
from ParkingManagerFourWheeler import ParkingManagerFourWheeler
from  models.Vehicle import Vehicle
from  models.Vehicle import VehicleType

class ParkingManagerFactory:

    def getParkingManager(self, vehicle: Vehicle):
        match vehicle.vehicleType:
            case VehicleType.TWO_WHEELER:
                return ParkingManagerTwoWheeler()
            case VehicleType.FOUR_WHEELER:
                return ParkingManagerFourWheeler
            case _:
                return None