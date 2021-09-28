my_student = {
    "name": "Rolf Smith",
    "grades": [70, 88, 90, 99]
}

def avarage_grade(student):
    return sum(student["grades"]) / len(student["grades"])

print(avarage_grade(my_student))