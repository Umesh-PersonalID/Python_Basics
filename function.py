# ========================================
# ✅ Python Functions: Full Intermediate-Level Revision
# ========================================

# 📌 1. WHAT IS A FUNCTION?
# A function is a block of reusable code that performs a specific task.
# Helps with modularity, readability, and reusability.

# ----------------------------------------
# 🔸 2. DEFINING AND CALLING FUNCTIONS
# ----------------------------------------

from re import X


def greet():
    print("Hello, world!")

greet()  # Calling the function

# Function with parameters
def add(a, b):
    return a + b

print("Addition:", add(3, 5))

# Function with default parameters
def power(base, exponent=2):
    return base ** exponent

print("Default exponent (square):", power(4))
print("Custom exponent (cube):", power(2, 3))

# ----------------------------------------
# 🔸 3. RETURNING MULTIPLE VALUES
# ----------------------------------------

def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

low, high, total = stats([1, 5, 10])
print("Min:", low, "Max:", high, "Sum:", total)

# ----------------------------------------
# 🔸 4. KEYWORD AND POSITIONAL ARGUMENTS
# ----------------------------------------

def intro(name, age):
    print(f"My name is {name}, and I am {age} years old.")

intro("Alice", 25)               # Positional
intro(age=30, name="Bob")        # Keyword arguments

# ----------------------------------------
# 🔸 5. VARIABLE NUMBER OF ARGUMENTS (*args, **kwargs)
# ----------------------------------------

# *args = variable-length positional arguments (tuple)
def sum_all(*args):
    return sum(args)

print("Sum of args:", sum_all(1, 2, 3, 4))

# **kwargs = variable-length keyword arguments (dict)
def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="Alice", age=25, location="NY")

# ----------------------------------------
# 🔸 6. LAMBDA (ANONYMOUS) FUNCTIONS
# ----------------------------------------

# One-line function
square = lambda x: x * x
print("Lambda square:", square(5))


# Lambda with map()
nums = [1, 2, 3]
squared = list(map(lambda x: x ** 2, nums))
print("Squared list using map + lambda:", squared)

# ----------------------------------------
# 🔸 7. HIGHER-ORDER FUNCTIONS (map, filter, reduce)
# ----------------------------------------

from functools import reduce

# map: apply function to all elements
print("Doubled list:", list(map(lambda x: x*2, [1, 2, 3])))

# filter: keep elements where function returns True
print("Filtered evens:", list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))

# reduce: combine all elements using a function
print("Product of list:", reduce(lambda x, y: x * y, [1, 2, 3, 4]))

# ----------------------------------------
# 🔸 8. NESTED FUNCTIONS & CLOSURES
# ----------------------------------------

def outer():
    msg = "Hi"
    def inner():
        print("Message from inner:", msg)
    return inner  # Returning the function

func = outer()
func()  # Calls inner()

# Closure: inner function remembers `msg` even after outer() is done

# ----------------------------------------
# 🔸 9. RECURSION
# ----------------------------------------

def factorial(n):
    '''hey this is for experiment'''
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))

# ----------------------------------------
# 🔸 10. DECORATORS (functions that modify other functions)
# ----------------------------------------

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# ----------------------------------------
# 🔸 11. FUNCTION ANNOTATIONS (Type Hints)
# ----------------------------------------

def greet_user(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."

print(greet_user("Charlie", 28))

# ----------------------------------------
# 🔸 12. KEY NOTES & TIPS
# ----------------------------------------

# ✅ Use default arguments carefully – they're evaluated once!
# ✅ Don't use mutable types (like lists) as default arguments
def bad_func(x=[]):  # ❌ will accumulate values
    x.append(1)
    return x

def good_func(x=None):  # ✅ safe way
    if x is None:
        x = []
    x.append(1)
    return x

print("Bad func:", bad_func())
print("Good func:", good_func())

# ✅ Use *args and **kwargs for flexible interfaces
# ✅ Functions are first-class citizens: pass them, return them, store in vars
# ✅ Use docstrings to describe purpose of functions

# Example of a docstring
def multiply(a: int, b: int) -> int:
    """Returns the product of a and b."""
    return a * b

print("Docstring:", multiply.__doc__)

# ========================================
# 🔚 End of Python Function Revision
# ========================================
print(factorial.__doc__)