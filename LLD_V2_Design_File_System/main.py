'''
Design File system

 Functional requirements:
- There are directories and files within it and we need to search for a particular file matching the search criteria
- Search criteria name, size or extension
- we can also search based on multiple criteria at once

Entities: USED COMPOSITE DESIGN PATTERN TO IMPLEMENT SEARCH CRITERIA AD FILE SYSTEM
- FileSystem
- Directory: name, list of filesystems, does searching of files while passing the search criteria
- File: name, size, extension, checks the filename based in the search criteria provided

- SearchCriteria: NameSearchCriteria, ExtensionSearchCriteria matches the given file name with the set search criteria requirements
- ANDSearchCriteria, ORSearchCriteria: returns success if all the search criteria are met
'''

from ANDSearchCriteria import ANDSearchCriteria
from ORSearchCriteria import ORSearchCriteria
from NameSearchCriteria import NameSearchCriteria
from ExtensionSearchCriteria import ExtensionSearchCriteria
from Directory import Directory
from File import File

andSearchCriteria = ORSearchCriteria([NameSearchCriteria('ayan'), ExtensionSearchCriteria('exe')])

file = File("ayan", 10, "exe")
file1 = File("ayan1", 10, "exe")

childDirectory = Directory("child Directory")
childDirectory.addFileSystem(file1)

rootDirectory = Directory("root Directory")
rootDirectory.addFileSystem(file)
rootDirectory.addFileSystem(childDirectory)

print(rootDirectory.dfs(andSearchCriteria))