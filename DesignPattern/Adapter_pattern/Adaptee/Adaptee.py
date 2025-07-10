from abc import ABC, abstractmethod

class Adaptee(ABC):

    @abstractmethod
    def getWeight(self):
        pass