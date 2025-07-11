from abc import ABC, abstractmethod
from Student import Student

class StudentBuilder:
    def __init__(self):
        self.rollNo = None
        self.age = None
        self.name = None
        
    def setRollNo(self, rollNo: int):
        self.rollNo = rollNo
        return self
    
    def setAge(self, age: int):
        self.age  = age
        return self
    
    def setName(self, name: str):
        self.name = name
        return self
    
    @abstractmethod
    def setFatherName(self):
        pass
    
    @abstractmethod
    def setMotherName(self):
        pass
    
    @abstractmethod
    def setSubjects(self):
        pass

    def build(self):
        return Student(self)