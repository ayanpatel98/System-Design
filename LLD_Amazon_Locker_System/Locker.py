from LockerStatus import LockerStatus
from LockerSize import LockerSize
from typing import Optional
from Package import Package

class Locker:
    def __init__(self, id: int, lockerSize: LockerSize):
        self.id = id
        self.lockerSize: LockerSize = lockerSize
        self.lockerStatus: LockerStatus = LockerStatus.AVAILABLE
        self.pickupCode: Optional[str] = None
        self.package: Optional[Package] = None