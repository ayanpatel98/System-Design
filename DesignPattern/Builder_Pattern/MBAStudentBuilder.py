from StudentBuilder import StudentBuilder

class MBAStudentBuilder(StudentBuilder):

    def __init__(self):
        # call super in order to initialize the  parent class attributes as well 
        # otherwise only child constructor attributes will be initialized
        super().__init__()
        self.subjects =[]
    
    def setFatherName(self, fatherName: str):
        self.fatherName  = fatherName
        return self
    
    def setMotherName(self, motherName: str):
        self.motherName = motherName
        return self
    
    def setSubjects(self):
        self.subjects =[]
        self.subjects.append("Business")
        self.subjects.append("Finance")
        return self