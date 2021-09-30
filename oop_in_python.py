my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99]
}


def avarage_grade(student):
    return sum(student["grades"]) / len(student["grades"])

print(avarage_grade(my_student))


class Student:
    def __init__(self, new_name, new_grades):
        self.name = new_name # name is not variable, it is a property of self. Creating name property inside self.
        self.grades = new_grades


    def avarage(self):
        return sum(self.grades) / len(self.grades)


student_one = Student("Rolf Smith", [70, 88, 90, 99])

print(student_one.name) # student_one becomes an object and name becomes property.
print(student_one.grades) # student_one becomes an object and grades becomes property.
print(student_one.avarage()) # avarage becomes a method.
print(Student.avarage(student_one)) # In the background class Student runs avarage method and passes student_one object inside the brackets.


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

matrix = Movie("The Matrix", 1999) # Assigning the to a matrix variable
print(matrix.name)
print(matrix.year)
print(Movie("The Matrix", 1999).name) # Calling class without assigning a variable


# Dunder "Magic" methods in Python.

class Garage:
    def __init__(self):
        self.cars = []

    def  __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f"<Garage {self.cars}>" # for code oriented description.

    def __str__(self):
        return f"Garage with {len(self)} cars." # for user oriented description.

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("BMW")

print(ford[0]) # Garage.__getitem__(ford, 0) is passing the same print function.
print(ford)