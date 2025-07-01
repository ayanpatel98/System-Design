from Vehicle import Vehicle
from strategy.SpecialDrive import SpecialDrive

class OffRoadVehicle(Vehicle):
    def __init__(self):
        super().__init__(SpecialDrive())