'''
Concept	                   Description
Class	            Blueprint for creating objects.
Object	            Instance of a class.
init()	            Constructor to initialize data when object is created.
Self	            Refers to the current object instance.
Attributes	        Variables associated with an object.
Methods	            Functions associated with a class.
Encapsulation	    Hiding internal state and requiring all interaction to be performed through an object’s methods.
Inheritance	        Ability of a class to inherit properties from another class.
Polymorphism	    Ability to use a unified interface for different data types.
Abstraction	        Hiding complex implementation details and showing only essential features.

'''

# ===========================================
# 📘 Python OOP Tutorial (Intermediate Level)
# ===========================================

# ✅ 1. CLASS & OBJECTS
class Dog:
    # Constructor
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Method
    def bark(self):
        print(f"{self.name} says Woof!")

# Creating objects
dog1 = Dog("Buddy", "Labrador")
dog2 = Dog("Max", "Poodle")

dog1.bark()
dog2.bark()

# ✅ 2. ENCAPSULATION
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Current Balance: ${acc.get_balance()}")
# print(acc.__balance) 

# acc.__balance  # ❌ Will give AttributeError (it's private)

# ✅ 3. INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

cat1 = Cat("Whiskers")
cat1.speak()

# ✅ 4. POLYMORPHISM
class Bird:
    def speak(self):
        print("Chirp!")

class Human:
    def speak(self):
        print("Hello!")

def make_speak(being):
    being.speak()

make_speak(Bird())
make_speak(Human())

# ✅ 5. ABSTRACTION via abc module
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(f"Area of circle: {circle.area()}")

# ✅ 6. SPECIAL METHODS / DUNDER METHODS
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' with {self.pages} pages"

    def __len__(self):
        return self.pages

book = Book("1984", 328)
print(book)           # Calls __str__
print(len(book))      # Calls __len__

# ✅ 7. CLASS VARIABLES vs INSTANCE VARIABLES
class Student:
    university = "XYZ University"  # class variable (shared)

    def __init__(self, name):
        self.name = name  # instance variable (unique)

student1 = Student("Alice")
student2 = Student("Bob")

print(student1.university)
print(student2.university)

student1.university = "ABC University"  # overrides for student1 only
print(student1.university)
print(student2.university)

# ✅ 8. STATIC & CLASS METHODS
class Utility:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def info(cls):
        print(f"This is a class method from {cls.__name__}")

print(Utility.add(3, 4))
Utility.info()

# ✅ 9. PROPERTY DECORATOR
class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

c = Celsius(25)
print(c.temperature)
c.temperature = 30
print(c.temperature)
# c.temperature = -300  # ❌ Raises ValueError
