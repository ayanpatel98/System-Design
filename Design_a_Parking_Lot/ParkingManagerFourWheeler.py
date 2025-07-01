from ParkingManager import ParkingManager
from FourWheelParkingSpot import FourWheelerParkingSpot

class ParkingManagerFourWheeler(ParkingManager):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):  # ensure __init__ runs once
            self.list = [FourWheelerParkingSpot(i) for i in range(5)]
            super().__init__(self.list)
            self._initialized = True
