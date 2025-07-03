from Button import Button
from ElevatorController import ElevatorController

class ExternalButton(Button):
    def __init__(self, floorNumber):
        self.floorNumber = floorNumber
        self.elevatorController = ElevatorController()

    def moveElevator(self):
        self.elevatorController.callElevator(self.floorNumber)