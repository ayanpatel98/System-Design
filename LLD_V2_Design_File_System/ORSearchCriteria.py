from SearchCriteria import SearchCriteria
from File import File

class ORSearchCriteria(SearchCriteria):

    def __init__(self, searchCriteriaList: list[SearchCriteria]):
        self.searchCriteriaList = searchCriteriaList

    def searchCriteria(self, file: File):
        return any(searchCriteria.searchCriteria(file) for searchCriteria in self.searchCriteriaList)