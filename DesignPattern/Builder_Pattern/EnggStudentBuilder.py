from StudentBuilder import StudentBuilder

class EnggStudentBuilder(StudentBuilder):

    def __init__(self):
        self.subjects =[]
        # self.rollNo = None
        # self.age = None
        # self.name = None
        self.fatherName = None
        self.motherName = None
    
    def setFatherName(self, fatherName: str):
        self.fatherName  = fatherName
        return self
    
    def setMotherName(self, motherName: str):
        self.motherName = motherName
        return self
    
    def setSubjects(self):
        self.subjects.append("OOPS")
        self.subjects.append("Algorithms")
        return self