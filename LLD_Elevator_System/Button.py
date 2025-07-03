from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def moveElevator(self):
        pass