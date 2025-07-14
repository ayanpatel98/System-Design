from abc import ABC, abstractmethod

class SearchCriteria(ABC):

    @abstractmethod
    def searchCriteria(self):
        pass