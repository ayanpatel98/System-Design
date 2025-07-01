from abc import ABC, abstractmethod

class Observable(ABC):

    @abstractmethod
    def add(self, observerObj):
        pass

    @abstractmethod
    def add(self, observerObj):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def setTemp(self, t):
        pass

    @abstractmethod
    def getTemp(self):
        pass
