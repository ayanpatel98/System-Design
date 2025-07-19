from State import State
from VendingMachine import VendingMachine
from States.AcceptMoneyState import AcceptMoneyState

class IdleState(State):

    def pressInsertButton(self, vendingMachine: VendingMachine):
        vendingMachine.state = AcceptMoneyState()

    def selectProductButton(self, vendingMachine: VendingMachine):
        pass

    def insertMoney(self, vendingMachine: VendingMachine):
        pass
    
    def insertProductCode(self, vendingMachine: VendingMachine):
        pass

    def cancel(self, vendingMachine: VendingMachine):
        pass

    def dispense(self, vendingMachine: VendingMachine):
        pass