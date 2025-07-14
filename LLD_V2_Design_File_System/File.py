from FileSystem import FileSystem
from SearchCriteria import SearchCriteria

class File(FileSystem):

    def __init__(self, name: str, size: int, extension: str):
        self.name = name
        self.size = size
        self.extension = extension
        self.isFile = True
    
    def dfs(self, searchCriteria: SearchCriteria):
        return searchCriteria.searchCriteria(self)