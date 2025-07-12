from Strategy.Strategy import Strategy
from Locker import Locker
from Package import Package
from typing import Optional
from LockerStatus import LockerStatus

class AssignmentStrategy(Strategy):

    def findLockerToAssign(self, lockers: list[Locker], package: Package)-> Optional[Locker]:
        for locker in sorted(lockers, key =  lambda x: x.lockerSize.value):
            if locker.lockerSize.value>=package.size.value and locker.lockerStatus==LockerStatus.AVAILABLE:
                return locker
        return None
        