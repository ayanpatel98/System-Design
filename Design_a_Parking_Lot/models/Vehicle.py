from models.VehicleType import VehicleType

class Vehicle:
    def __init__(self, vehicleNo, vehicleType: VehicleType):
        self.vehicleNo = vehicleNo
        self.vehicleType = vehicleType