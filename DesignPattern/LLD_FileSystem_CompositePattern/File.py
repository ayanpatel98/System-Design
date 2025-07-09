from FileSystem import FileSystem
from FileSystemType import FileSystemType

class File(FileSystem):

    def __init__(self, name: str):
        self.name = name
        self.type = FileSystemType.FILE
    
    def search(self, name: str):
        if name==self.name:
            return True        
    
    def ls(self):
        print("file name: ", self.name)