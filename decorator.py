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


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school) # super() is a parent class which is Student
        self.salary = salary
    
    @property   # property decorator enables weekly_salary to act as an object not as methos. You can call weekly_salary() without brackets.
    def weekly_salary(self):
        return self.salary * 37.5
    

rolf = WorkingStudent("Rolf", "MIT", 25.50)
# print(rolf.weekly_salary()) 
print(rolf.weekly_salary)