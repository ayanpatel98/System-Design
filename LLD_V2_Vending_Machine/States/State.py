from abc import ABC, abstractmethod

class State(ABC):

    @abstractmethod
    def pressInsertButton(self):
        pass

    @abstractmethod
    def selectProductButton(self):
        pass

    @abstractmethod
    def insertMoney(self):
        pass

    @abstractmethod
    def insertProductCode(self):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def dispense(self):
        pass