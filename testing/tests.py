from domain.student import Student


class Test:

    def run_student_creation_test(self):
        print("create student test...")
        id_student = 23
        name = "Jordan"
        value = 9000.1
        student = Student(id_student,name,value)
        assert id_student==student.id_student
        print("student test created successfully...")