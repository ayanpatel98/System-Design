from ParkingManager import ParkingManager
from TwoWheelParkingSpot import TwoWheelerParkingSpot

class ParkingManagerTwoWheeler(ParkingManager):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):  # ensure __init__ runs once
            self.list = [TwoWheelerParkingSpot(i) for i in range(10)]
            super().__init__(self.list)
            self._initialized = True
