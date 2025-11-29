from business.student_service import StudentService
from infrastructure.repository_students import StudentRepository
from presentation.console import Console
from testing.tests import Test
from validation.student_validator import StudentValidator

test = Test()
test.run_student_creation_test()
repository_students = StudentRepository()
validator_student = StudentValidator()
service_students = StudentService(validator_student,repository_students)
console = Console(service_students)
console.run()