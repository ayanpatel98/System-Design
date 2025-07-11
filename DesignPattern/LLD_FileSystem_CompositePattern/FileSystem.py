from abc import ABC, abstractmethod

class FileSystem(ABC):

    @abstractmethod
    def ls(self):
        pass

    @abstractmethod
    def search(self):
        pass