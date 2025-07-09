from FileSystem import FileSystem
from FileSystemType import FileSystemType

class Directory(FileSystem):

    def __init__(self, name: str):
        self.name = name
        self.fileSystemList: list[FileSystem] = []
        self.type = FileSystemType.DIRECTORY

    def add(self, fileSystem: FileSystem):
        self.fileSystemList.append(fileSystem)
    
    def search(self, name):
        for fileSystem in self.fileSystemList:
            if fileSystem.search(name):
                return True
        return False
    
    def ls(self):
        print("Directory: ", self.name, "-> ", end="")

        for fileSystem in self.fileSystemList:
            fileSystem.ls()