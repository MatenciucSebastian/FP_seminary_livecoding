from domain.student import Student


class StudentService:

    def __init__(self,student_validator,repository_students):
        self.__student_validator = student_validator
        self.__repository_students = repository_students

    def add_student(self,id_student,name,value):
        student = Student(id_student,name,value)
        self.__student_validator.validate_student(student)
        self.__repository_students.add_student(student)

    def get_all_students(self):
        return self.__repository_students.get_all()