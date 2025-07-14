from SearchCriteria import SearchCriteria
from File import File

class NameSearchCriteria(SearchCriteria):
    def __init__(self, name: str):
        self.name = name

    def searchCriteria(self, file: File):
        return file.name==self.name
        