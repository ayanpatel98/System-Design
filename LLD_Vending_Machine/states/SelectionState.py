from State import State
from VendingMachine import VendingMachine
from IdleState import IdleState
from DispenseState import DispenseState

class SelectionState(State):

    def __init__(self):
        pass
    
    def pressInsertCashButton(self, vendingMachine:VendingMachine):
        pass
    
    def insertMoney(self, vendingMachine: VendingMachine):
        pass
    
    def selectProductButton(self, vendingMachine:VendingMachine):
        pass
    
    def chooseProduct(self, vendingMachine:VendingMachine, itemCode: int):
        if not vendingMachine.inventory.removeFromInvetory(itemCode):
            print("product sold out")
        product  = vendingMachine.inventory.getProduct(itemCode)
        if not product:
            print("incorrect product code")
            return
        
        if vendingMachine.currentMoney<product.item.price:
            print("insufficient Money")
            self.refundButton(vendingMachine)
        elif vendingMachine.currentMoney>=product.item.price:
            vendingMachine.inventory.removeFromInvetory(product.itemCode)
            if vendingMachine.currentMoney>product.item.price:
                print(vendingMachine.currentMoney-product.item.price)
            
            vendingMachine.machineState = DispenseState(vendingMachine, product.itemCode)
        
    
    def refundButton(self, vendingMachine: VendingMachine):
        vendingMachine.removeMoney()
        vendingMachine.machineState = IdleState()
        return
    
    def dispenseProduct(self, vendingMachine:VendingMachine):
        pass

    def addToInventory(self, vendingMachine:VendingMachine):
        pass