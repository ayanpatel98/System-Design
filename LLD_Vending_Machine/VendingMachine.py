from Inventory import Inventory
from states.State import State
from states.IdleState import IdleState

class VendingMachine:
    def __init__(self):
        self.inventory = Inventory(10)
        self.machineState = IdleState()
        self.currentMoney = 0
    
    def removeMoney(self):
        self.currentMoney = 0
    
    def addMoney(self, money: int):
        self.currentMoney+=money
