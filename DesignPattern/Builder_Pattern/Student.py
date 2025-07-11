class Student:

    def __init__(self, studentBuilder):
        print(studentBuilder.name)
        self.rollNo = studentBuilder.rollNo
        self.age = studentBuilder.age
        self.name = studentBuilder.name
        self.fatherName = studentBuilder.fatherName
        self.motherName = studentBuilder.motherName
        self.subjects = studentBuilder.subjects