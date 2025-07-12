"""
functional: 
-user should be able to pickup the packages
- delivery partners should place the package in the right locker

entities:
- enums: LockerSize, LockerStatus
- locker: id, size, code, package, status
- package: id, size, 
- lockerService: add locker, list of lockers, assign to locker, pickup package
- lockerAssignmentStrategy: assignLockerStrategy logic
"""

from Locker import Locker
from Package import Package
from LockerStatus import LockerStatus
from LockerSize import LockerSize
from LockerService import LockerService
from Strategy.AssignmentStrategy import AssignmentStrategy

package1 = Package(1, LockerSize.LARGE)
package2 = Package(2, LockerSize.SMALL)
package3 = Package(3, LockerSize.MEDIUM)
package4 = Package(4, LockerSize.LARGE)

lockerService = LockerService(AssignmentStrategy())
lockerService.addLocker(LockerSize.SMALL)
lockerService.addLocker(LockerSize.MEDIUM)
lockerService.addLocker(LockerSize.LARGE)

code = lockerService.assignLocker(package1)
lockerService.assignLocker(package4)
print(lockerService.lockerLog)
lockerService.pickupPackage(code)
lockerService.assignLocker(package4)
print(lockerService.lockerLog)