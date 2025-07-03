from Elevator import Elevator
from Directions import Directions

class ElevatorController:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = ElevatorController()
        return cls._instance

    def __init__(self, totalFloors: int, elevatorList: List[Elevator]):
        if not hasattr(self, "_initialized"):
            # self.elevatorList = [Elevator(i, 0) for i in range(0, totalElevators)]
            self.elevatorList = elevatorList
            self.totalFloors = totalFloors
            self._initialized = True

    def moveElevator(self, floorNumber: int, elevatorNumber: int):
        if elevatorNumber>=len(self.elevatorList):
            return
        
        elevator = self.elevatorList[elevatorNumber]
        self.updateElevatorDirection(elevator)
        
        elevator.targetFloors.append(floorNumber)

    def callElevator(self, floorNumber: int):
        nearestElevatorList = sorted(self.elevatorList, key=lambda x: abs(x.currFloor-floorNumber))
        elevator = nearestElevatorList[0]
        self.updateElevatorDirection(elevator)

        elevator.targetFloors.append(floorNumber)
    
    def updateElevatorDirection(self, elevator: Elevator):
        if elevator.currFloor>elevator.targetFloors[0]:
            elevator.direction = Directions.DOWN
        elif elevator.currFloor<elevator.targetFloors[0]:
            elevator.direction = Directions.UP
        else:
            elevator.direction = Directions.IDLE
    
    # Stop to the neaerest floor and update directions to IDLE
    def stopAllElevators(self):
        for elevator in self.elevatorList:
            if elevator.direction==Directions.UP:
                if elevator.currFloor < self.totalFloors-1:
                    elevator.currFloor+=1
            elif elevator.direction==Directions.DOWN:
                if elevator.currFloor > 0:
                    elevator.currFloor-=1
            elevator.direction = Directions.IDLE
