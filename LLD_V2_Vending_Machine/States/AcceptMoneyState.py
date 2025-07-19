from State import State
from VendingMachine import VendingMachine
from ChooseProductState import ChooseProductState
from IdleState import IdleState

class AcceptMoneyState(State):

    def pressInsertButton(self, vendingMachine: VendingMachine):
        pass

    def selectProductButton(self, vendingMachine: VendingMachine):
        vendingMachine.state = ChooseProductState()

    def insertMoney(self, vendingMachine: VendingMachine, amount: int):
        vendingMachine.availableMoney+=amount
    
    def insertProductCode(self, vendingMachine: VendingMachine):
        pass

    def cancel(self, vendingMachine: VendingMachine):
        money = vendingMachine.availableMoney
        vendingMachine.availableMoney = 0
        vendingMachine.state = IdleState()
        return money

    def dispense(self, vendingMachine: VendingMachine):
        pass