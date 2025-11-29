from errors.exceptions import ValidationError


class StudentValidator:

    def validate_student(self,student):
        errors = ""
        if student.id_student <0:
            errors +="invalid id!\n"
        if student.name == "":
            errors +="invalid name!\n"
        if student.value <=0.0:
            errors +="invalid value!\n"
        if len(errors)>0:
            raise ValidationError(errors)