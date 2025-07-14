from SearchCriteria import SearchCriteria
from File import File

class ExtensionSearchCriteria(SearchCriteria):
    def __init__(self, extension: str):
        self.extension = extension

    def searchCriteria(self, file: File):
        return file.extension==self.extension
        