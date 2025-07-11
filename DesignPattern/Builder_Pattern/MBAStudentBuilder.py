from StudentBuilder import StudentBuilder

class MBAStudentBuilder(StudentBuilder):

    def __init__(self):
        self.subjects =[]
        self.fatherName = None
        self.motherName = None
    
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