from abc import ABC, abstractmethod

class Strategy(ABC):

    @abstractmethod
    def findLockerToAssign(self):
        pass