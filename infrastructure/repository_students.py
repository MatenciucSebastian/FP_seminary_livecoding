from errors.exceptions import RepositoryError


class StudentRepository:

    def __init__(self):
        self.__students = {}

    def add_student(self,student):
        id_student = student.id_student
        if id_student in self.__students:
            raise RepositoryError("id already exists!")
        self.__students[id_student]=student

    def get_all(self):
        return list(self.__students.values())