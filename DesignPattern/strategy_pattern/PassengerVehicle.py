from Vehicle import Vehicle
from strategy.NormalDrive import NormalDrive

class PassengerVehicle(Vehicle):
    def __init__(self):
        super().__init__(NormalDrive())