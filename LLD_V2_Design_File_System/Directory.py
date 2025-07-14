from FileSystem import FileSystem
from SearchCriteria import SearchCriteria

class Directory(FileSystem):

    def __init__(self, name: str):
        self.name = name
        self.fileSystemList: list[FileSystem] = []
        self.isFile = False
    
    def addFileSystem(self, fileSystem: FileSystem):
        self.fileSystemList.append(fileSystem)
    
    def dfs(self, searchCriteria: SearchCriteria):
        for fileSystem in self.fileSystemList:
            if fileSystem.dfs(searchCriteria):
                return True
        return False