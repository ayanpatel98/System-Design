from InternalButton import InternalButton
from Floor import Floor
from Display import Display
from Direction import Direction
import collections

class Elevator:
    def __init__(self, id: int, initialFloor: int):
        self.id = id
        self.internalButton = InternalButton()
        self.targetFloorList = collections.deque([])
        self.currentFloor: Floor = initialFloor
        self.direction = Direction.UP
        self.display = Display(id, self.currentFloor, self.direction)
    
    def pressInternalButton(self, floorNumber: int):
        self.internalButton.goToFloor(floorNumber, self)
    
    def showDisplay(self):
        self.display(self.currentFloor, self.direction)
    
    def updateDirection(self, floorNumber: int):
        if self.targetFloorList and floorNumber>self.targetFloorList[0] and self.direction==Direction.DOWN:
            self.direction = Direction.UP
        elif  self.targetFloorList and floorNumber<self.targetFloorList[0] and self.direction==Direction.UP:
            self.direction = Direction.DOWN
        else:
            self.direction = Direction.IDLE

    def updateFloor(self, floorNumber: int):
        self.currentFloor = floorNumber