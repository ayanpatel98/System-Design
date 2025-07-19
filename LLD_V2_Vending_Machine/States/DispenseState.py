from State import State
from VendingMachine import VendingMachine
from Item import Item
from IdleState import IdleState

class DispenseState(State):

    def pressInsertButton(self, vendingMachine: VendingMachine):
        pass

    def selectProductButton(self, vendingMachine: VendingMachine):
        pass

    def insertMoney(self, vendingMachine: VendingMachine):
        pass
    
    def insertProductCode(self, vendingMachine: VendingMachine):
        pass

    def cancel(self, vendingMachine: VendingMachine):
        pass

    def dispense(self, vendingMachine: VendingMachine, code: Item):
        product = vendingMachine.getProduct(code)
        vendingMachine.updateSoldOutItem(code)
        vendingMachine.state  = IdleState()
        return product