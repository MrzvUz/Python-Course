from oop_in_python import avarage_grade


class  Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

student_details = Student("Rolf", "Shcool_Name")

student_details.marks.append(90)

print(student_details.school)
print(student_details.name)
print(student_details.marks)


class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.salary = salary
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = WorkingStudent("Rolf", "MIT", 25.50)
print(rolf.salary )
print(rolf.name)
print(rolf.school)

print("---------------------------------------------")

# Inheritance.

class  Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


student_details = Student("Rolf", "Shcool_Name")

student_details.marks.append(90)
student_details.marks.append(85)

print(student_details.school)
print(student_details.name)
print(student_details.marks)
print(student_details.average())



class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # super() is a parent class which is Student
        self.salary = salary
    
    def weekly_salary(self):
        return self.salary * 37.5
    

rolf = WorkingStudent("Rolf", "MIT", 25.50)
print(rolf.salary )
print(rolf.name)
print(rolf.school)
rolf.marks.append(88)
rolf.marks.append(99)
print(rolf.average())
print(rolf.weekly_salary())
