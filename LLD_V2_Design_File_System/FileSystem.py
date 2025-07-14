from abc import ABC, abstractmethod

class FileSystem(ABC):

    @abstractmethod
    def dfs(self):
        pass