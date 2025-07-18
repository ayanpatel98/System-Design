from Button import Button
from Elevator import Elevator
from ElevatorController import ElevatorController

class InternalButton(Button):
    def __init__(self):
        self.elevatorController = ElevatorController()

    def goToFloor(self, floorNumber: int, elevator: Elevator):
        self.elevatorController.goToFloor(floorNumber, elevator)