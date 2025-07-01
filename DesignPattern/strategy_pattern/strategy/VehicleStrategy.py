from abc import ABC, abstractmethod

class VehicleStrategy(ABC):

    @abstractmethod
    def drive(self):
        pass