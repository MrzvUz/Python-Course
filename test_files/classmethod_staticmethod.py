class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


rolf = Student("Rolf", "MIT") # rolf object of Student class.

rolf.marks.append(88)
rolf.marks.append(97)

print(rolf.average())


print("--------------------------------------------")


class Foo:
    @classmethod    # if we want to access class Foo.
    def hi(cls):    # cls stands for class.
        print(cls.__name__) # Accesses the class and prints out the name of the class which is Foo.

my_object = Foo()
my_object.hi()


class Bar:
    @staticmethod   # if we want to access method which is hi()
    def hi():   # when we use @staticmethod, method doesn't take parameters
        print("Hello, I don't take parameters")

another_object = Bar()
another_object.hi()


print("--------------------------------------------")


# Better example with @staticmethod

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount    # we have __init__ method, in which amount property gets initialized in (self.amount) the object

    def __repr__(self):     # we have a __repr__(self) repr method which return string representing the object 
        return f"<FixedFloat {self.amount:.2f}>" # .2f is going to print two amount of decimal places. 2.5909 will be 2.59

    @staticmethod
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)


new_number = FixedFloat.from_sum(19.858, 0.789)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


money = Euro(18.786)
print(money)


print("--------------------------------------------")


# Better example with @classmethod and @classmethod better than @staticmethod.

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount    # we have __init__ method, in which amount property gets initialized in (self.amount) the object

    def __repr__(self):     # we have a __repr__(self) repr method which return string representing the object 
        return f"<FixedFloat {self.amount:.2f}>" # .2f is going to print two amount of decimal places. 2.5909 will be 2.59

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


new_number = FixedFloat.from_sum(19.858, 0.789)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"

    def __repr__(self):
        return f"<Euro {self.symbol}{self.amount:.2f}>"


money = Euro.from_sum(18.786, 9.999)
print(money)
