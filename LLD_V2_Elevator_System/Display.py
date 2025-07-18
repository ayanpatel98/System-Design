from Floor import Floor
from Direction import Direction

class Display:
    def __init__(self, id: int, floor: Floor, direction: Direction):
        self.id = id
        self.currFloor = floor
        self.direction = direction

    def showDisplay(self, currentFloor: Floor, direction: Direction):
        print(currentFloor.number)
        print(direction)