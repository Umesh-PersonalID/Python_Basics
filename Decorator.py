#Decorators modify or extend the behavior of a function.

#They are higher-order functions.'

#using decorator we can add ectra feature to existing function without touching the function, If we dont have the access of the function.
# Define a basic decorator
def my_decorator(func):                      # O(1) – just function definition
    def wrapper():                           # O(1) – wrapper defined
        print("Before function call")        # O(1)
        func()                               # O(1) – depends on the decorated function
        print("After function call")         # O(1)
    return wrapper                           # O(1)

# A simple function
@my_decorator                                # O(1) – decorator applied
def say_hello():
    print("Hello!")

say_hello()  # Output: Before → Hello! → After