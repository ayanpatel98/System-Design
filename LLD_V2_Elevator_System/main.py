'''
Elevator System:

functional:
- user able to call the elevator using buttons from the floor and able to move the elevator to a floor
- display the floor and direction in the elevator

entities:
enums: Direction
- Floor: number, ExternalButton
- InternalButton: goToFloor(FloorNumber)
- ExternalButton: callElevator(Floorumber)
- Display: id, currentFloor, direction
- Elevator: id, InternalButton, Display, currentFloor, direction, targetFloorList, showDisplay, addToTargetList, pressInternalButton
- ElevatorController: list of elevators, goToFloor(FloorNumber), callElevator(FloorNumber)
'''