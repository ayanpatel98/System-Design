from Directions import Directions
from InternalButton import InternalButton

class Elevator:
    
    def __init__(self, id: int, currFloor: int):
        self.id = id
        self.currFloor = currFloor
        self.targetFloors = []
        self.direction = Directions.IDLE
        self.internalButton = InternalButton()
