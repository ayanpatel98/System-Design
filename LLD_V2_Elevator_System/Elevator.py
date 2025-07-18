from InternalButton import InternalButton
from Floor import Floor
from Display import Display
from Direction import Direction

class Elevator:
    def __init__(self, id: int, initialFloor: int):
        self.id = id
        self.internalButton = InternalButton()
        self.targetFloorList = []
        self.currentFloor: Floor = initialFloor
        self.direction = Direction.UP
        self.display = Display(id, self.currentFloor, self.direction)

    def addToTarget(self, floor: Floor):
        self.targetFloorList.append(floor)
    
    def pressInternalButton(self, floorNumber: int):
        self.internalButton.goToFloor(floorNumber, self)
    
    def showDisplay(self):
        self.display(self.currentFloor, self.direction)
    
    def updateDirection(self, floorNumber: int):
        if floorNumber>self.currentFloor and self.direction==Direction.DOWN:
            self.direction = Direction.UP
        else:
            self.direction = Direction.DOWN

    def updateFloor(self, floorNumber: int):
        self.currentFloor = floorNumber