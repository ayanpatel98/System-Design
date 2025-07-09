from State import State
from VendingMachine import VendingMachine
from IdleState import IdleState

class DispenseState(State):
    
    def __init__(self, vendingMachine: VendingMachine, productCode: int):
        self.dispenseProduct(vendingMachine, productCode)
    
    def pressInsertCashButton(self, vendingMachine: VendingMachine):
        pass
    
    def insertMoney(self, vendingMachine: VendingMachine):
        pass
    
    def selectProductButton(self, vendingMachine: VendingMachine):
        pass
    
    def chooseProduct(self, vendingMachine: VendingMachine):
        pass
    
    def refundButton(self, vendingMachine: VendingMachine):
        pass
    
    def dispenseProduct(self, vendingMachine: VendingMachine, productCode: int):
        vendingMachine.inventory.removeFromInvetory(productCode)
        vendingMachine.machineState = IdleState()
        print("Prduct Dispensed")

    def addToInventory(self, vendingMachine: VendingMachine):
        pass