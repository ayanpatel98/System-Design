from abc import ABC, abstractmethod

class Adapter(ABC):

    @abstractmethod
    def getWeightInKg(self):
        pass