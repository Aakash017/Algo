class car:
    type = "sedan only"

    def __init__(self, name, mileage):  # constructor method
        self.name = name
        self.mileage = mileage

    def describe(self):  # instance method
        print("%s gives mileage=%s " % (self.name, self.mileage))


c = car("Honda", 22)
print(c)
c.describe()
print(c.type)

"Inheritance"


class BMW(car):
    pass


b = BMW("MCD", 10)

b.describe()

"Encapsulation"


class DOG:
    def __init__(self, name, breed, age):
        self.__name = name #Private
        self.breed = breed #Public
        self._age = age #Protected

    def info(self):
        print("This is %s from %s family" % (self.__name, self.breed))


d = DOG("Tyson", "bully", 10)
d.info()
print(d.breed)
print(d._age)
print(d._DOG__name)


class SYB(DOG):
    pass


# print(s._name)


class PIT(SYB):
    pass


# p = PIT("Pitbul", "pitbull")
# p.info()
# print(p._name)


from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, name):
        self.name = name

    def description(self):
        print("This the description function of class car.")

    @abstractmethod
    def price(self, x):
        pass


class new(Car):
    def price(self, x):
        print(f"The {self.name}'s price is {x} lakhs.")


obj = new("Honda City")

obj.description()
obj.price(25)

diff = "Difference between static method and class method means - class method use class as first parameter" \
       "while static method does not require cls as first perm"

print(diff)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birth_year(self):
        print(f"executing foo({self})")
        print(f'{self.name} is {self.age} years old')

    @classmethod
    def birth_year_2(cls, name, age):
        print(f"executing class_foo({cls})")
        print(f'{name} is {age} years old')

    @staticmethod
    def birth_year_3(name, age):
        print(f'{name} is {age} years old')


p = Person("Aakash", 25)
p.birth_year()
p.birth_year_2("Aakash", 23)
p.birth_year_3("Aakash", 21)

P = Person("Bablu", 26)
print("Calling class fns")
P.birth_year_2("Bable", 22)
P.birth_year()

Person.birth_year_3("Vijat", 33)

"""
So class methods which we can call directly using class , no instance is required, however inbuilt methods are those
where instance is required same as for static
now between instance methods and static methods are in instance methods - class as first perm require
but in static it is not required
"""

"""
Instance methods need a class instance and can access the instance through self . 
Class methods don't need a class instance. 
They can't access the instance ( self ) but they have access to the class itself via cls .
Static methods don't have access to cls or self .
"""


# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
    stream = 'cse'  # Class Variable

    def __init__(self, name, roll):
        self.name = name  # Instance Variable
        self.roll = roll  # Instance Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream)  # prints "cse"
print(b.stream)  # prints "cse"
print(a.name)  # prints "Geek"
print(b.name)  # prints "Nerd"
print(a.roll)  # prints "1"
print(b.roll)  # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream)  # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream)  # prints 'ece'
print(b.stream)  # prints 'cse'

# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream)  # prints 'mech'
print(b.stream)  # prints 'mech'


