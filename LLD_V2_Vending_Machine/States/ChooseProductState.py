from State import State
from VendingMachine import VendingMachine
from DispenseState import DispenseState
from IdleState import IdleState

class ChooseProductState(State):

    def pressInsertButton(self, vendingMachine: VendingMachine):
        pass

    def selectProductButton(self, vendingMachine: VendingMachine):
        pass

    def insertMoney(self, vendingMachine: VendingMachine):
        pass
    
    def insertProductCode(self, vendingMachine: VendingMachine, code: int):
        # code valid
        if not vendingMachine.checkValidity(code):
            return False

        # product out of stock
        if not vendingMachine.checkStock(code):
            return False

        # check if the money inserted if enough
        product = vendingMachine.getProduct(code)
        if product.price>vendingMachine.availableMoney:
            self.cancel(vendingMachine)
            return False
        
        # is availabe then dispense and return the change
        change = vendingMachine.availableMoney-product.price
        vendingMachine.state = DispenseState()
        vendingMachine.state.dispense(vendingMachine, code)
        return change

    def cancel(self, vendingMachine: VendingMachine):
        money = vendingMachine.availableMoney
        vendingMachine.availableMoney = 0
        vendingMachine.state = IdleState()
        return money

    def dispense(self, vendingMachine: VendingMachine):
        pass