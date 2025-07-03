from Elevator import Elevator
from InternalButton import InternalButton
from ExternalButton import ExternalButton
from ElevatorController import ElevatorController

if __name__=="__main__":
    elevator1 = Elevator(1, 0)
    elevator2 = Elevator(2, 0)
    elevator3 = Elevator(3, 0)

    elvController = ElevatorController(15, [elevator1, elevator2, elevator3])

    externalButton = ExternalButton(3) # External button at floor 3

    elevator1.internalButton.moveElevator(5, elevator1.id)