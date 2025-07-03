from Button import Button
from ElevatorController import ElevatorController

class InternalButton(Button):
    def __init__(self):
        self.elevatorController = ElevatorController()
    
    def moveElevator(self, floorNumber: int, elevatorNumber: int):
        self.elevatorController.moveElevator(floorNumber, elevatorNumber)