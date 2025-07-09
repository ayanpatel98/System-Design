from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def pressInsertCashButton(self):
        pass
    
    @abstractmethod
    def insertMoney(self):
        pass
    
    @abstractmethod
    def selectProductButton(self):
        pass
    
    @abstractmethod
    def chooseProduct(self):
        pass
    
    @abstractmethod
    def refundButton(self):
        pass
    
    @abstractmethod
    def dispenseProduct(self):
        pass

    @abstractmethod
    def addToInventory(self):
        pass