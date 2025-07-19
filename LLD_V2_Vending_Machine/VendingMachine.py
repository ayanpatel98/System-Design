from Inventory import Inventory
from States.IdleState  import IdleState

class VendingMachine:
    def __init__(self):
        self.inventory = Inventory()
        self.state = IdleState()
        self.availableMoney = 0
    
    def getVendingMachineState(self):
        return self.state
    
    def checkValidity(self, code: int):
        if code<0 and code>=len(self.inventory):
            return False
        return True
    
    def checkStock(self, code: int):
        for shelf in self.inventory.shelfList:
            if shelf.code==code:
                if not shelf.issoldOut:
                    return True
                else:
                    return False
    
    def getProduct(self, code: int):
        for shelf in self.inventory.shelfList:
            if shelf.code==code:
                return shelf.item
            
    def updateSoldOutItem(self, code: int):
        for shelf in self.inventory.shelfList:
            if shelf.code==code:
                shelf.issoldOut = True
