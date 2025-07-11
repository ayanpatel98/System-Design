from EnggStudentBuilder import EnggStudentBuilder
from MBAStudentBuilder import MBAStudentBuilder
from Student import Student

sb = EnggStudentBuilder()

student = sb.setAge(10).setRollNo(51).setName("Ayan").setSubjects().build()
print(student.fatherName)