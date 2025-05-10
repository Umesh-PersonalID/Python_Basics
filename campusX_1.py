#Basic Types - Int, Float, String, complex
#COntainer Types - list,tuple,set,dictionary
#User Defined Types - class

#Dynamic Binding
#static Binding
# Dynamic Typing
#Variable's type is determined at runtime.That is dynamic typing. python is dynamic typing language
#Static Typing
#Variable's type is known at compile time.c++,java


class A:
    def show(self):
        print("A's show")

obj = A()
obj.show()  # Static binding: Python already knows `show()` refers to A's method, at compile time


class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

obj = B()
obj.show()  # Dynamic binding: calls B's version at runtime, at run time



class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

# Python allows this
def make_animal_talk(animal):
    animal.speak()  # Dynamic Binding — resolved at runtime

a = Dog()           # Dynamic Typing — variable type not declared
make_animal_talk(a) # Output: Bark
