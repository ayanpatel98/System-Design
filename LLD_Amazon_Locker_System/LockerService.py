from LockerSize import LockerSize
from LockerStatus import LockerStatus
from Locker import Locker
from Package import Package
from Strategy.Strategy import Strategy
from typing import Optional
import random

class LockerService:
    def __init__(self, assignmentStrategy: Strategy):
        self.lockers: list[Locker] = []
        self.assignmentStrategy: Strategy = assignmentStrategy
        self.lockerLog = {}
    
    def addLocker(self, size: LockerSize):
        self.lockers.append(Locker(len(self.lockers)+1, size))
        print("Locker Added")
    
    def assignLocker(self, package: Package)-> str:
        lockerAvailable: Optional[Locker] = self.assignmentStrategy.findLockerToAssign(self.lockers, package)
        if not lockerAvailable:
            print("Locker Not Available for package id: ", package.id)
            return
        
        lockerAvailable.lockerStatus = LockerStatus.NOT_AVAILABLE
        lockerAvailable.pickupCode = str(random.randint(1, 1000))
        lockerAvailable.package = package
        self.lockerLog[lockerAvailable.pickupCode] = lockerAvailable
        print("Locker Assigned with locker code: ", lockerAvailable.pickupCode)
        return lockerAvailable.pickupCode

    def releaseLocker(self, locker: Locker):
        locker.lockerStatus = LockerStatus.AVAILABLE
        locker.pickupCode = None
        locker.package = None

    def pickupPackage(self, pickupCode: str):
        if pickupCode not in self.lockerLog:
            print("Package Not Available")
            return
        
        locker: Locker = self.lockerLog[pickupCode]

        self.releaseLocker(locker)
        del self.lockerLog[pickupCode]
        print("Package Picked Up")
        return


