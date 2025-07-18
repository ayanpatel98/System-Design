from Elevator import Elevator

class ElevatorController:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = ElevatorController()
        return cls._instance

    def __init__(self, totalFloors: int):
        if not hasattr(self, "_initialized"):
            self.elevatorlist: list[Elevator] = []
            self.totalFloors = totalFloors

    def addElevator(self, elevator: Elevator):
        self.elevatorlist.append(elevator)
    
    def goToFloor(self, floorNumber: int, elevator: Elevator):
        if floorNumber>self.totalFloors or floorNumber<1:
            return
        elevator.addToTarget(floorNumber)

    def callElevator(self, floorNumber: int):
        elevatorList = sorted(self.elevatorlist, key= lambda elevator: abs(elevator.currentFloor-floorNumber))
        elevator = elevatorList[0]

        elevator.updateDirection(floorNumber)
        elevator.updateFloor(floorNumber)

        
            
