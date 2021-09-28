my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99]
}


def avarage_grade(student):
    return sum(student["grades"]) / len(student["grades"])

print(avarage_grade(my_student))


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades


    def avarage(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Rolf Smith", [70, 88, 90, 99])

print(student_one.name) # student_one becomes an object and name becomes property.
print(student_one.grades) # student_one becomes an object and grades becomes property.
print(student_one.avarage()) # avarage becomes a method.
print(Student.avarage(student_one)) # In the background class Student runs avarage method and passes student_one object inside the brackets.