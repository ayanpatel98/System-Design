from State import State
from VendingMachine import VendingMachine
from IdleState import IdleState
from SelectionState import SelectionState

class HasMoneyState(State):

    def __init__(self):
        pass
    
    def pressInsertCashButton(self, vendingMachine:VendingMachine):
        pass
    
    def insertMoney(self, money: int, vendingMachine: VendingMachine):
        vendingMachine.addMoney(money)
    
    def selectProductButton(self, vendingMachine:VendingMachine):
        vendingMachine.machineState = SelectionState()
    
    def chooseProduct(self, vendingMachine:VendingMachine):
        pass
    
    def refundButton(self, vendingMachine: VendingMachine):
        vendingMachine.removeMoney()
        vendingMachine.machineState = IdleState()
    
    def dispenseProduct(self, vendingMachine:VendingMachine):
        pass

    def addToInventory(self, vendingMachine:VendingMachine):
        pass