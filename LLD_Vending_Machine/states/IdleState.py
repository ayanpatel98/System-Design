from State import State
from VendingMachine import VendingMachine
from HasMoneyState import HasMoneyState

class IdleState(State):

    def __init__(self):
        pass
    
    def pressInsertCashButton(self, vendingMachine: VendingMachine):
        vendingMachine.machineState = HasMoneyState()
    
    def insertMoney(self, vendingMachine:VendingMachine):
        pass
    
    def selectProductButton(self, vendingMachine:VendingMachine):
        pass
    
    def chooseProduct(self, vendingMachine:VendingMachine):
        pass
    
    def refundButton(self, vendingMachine:VendingMachine):
        pass
    
    def dispenseProduct(self, vendingMachine:VendingMachine):
        pass

    def addToInventory(self, vendingMachine:VendingMachine, price:int, itemType):
        vendingMachine.inventory.updateInventory(price, itemType)
    