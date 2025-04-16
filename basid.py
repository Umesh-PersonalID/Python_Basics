# 1. User Input / Output
# Getting input from the user and displaying output
name = input("Enter your name: ")  # Takes user input #always string
print("Hello,", name)  # Prints output

# 2. Data Types
# Demonstrating basic data types in Python
integer_var = 10       # Integer
float_var = 10.5       # Float
string_var = "Hello"   # String
bool_var = True        # Boolean
print(type(integer_var), type(float_var), type(string_var), type(bool_var))

# 3. If-Else Statements
# Conditional execution based on a condition
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4. Switch Statement (Python uses dictionary-based approach as it lacks switch-case)
def switch_demo(value):
    switch_dict = {
        1: "One",
        2: "Two",
        3: "Three"
    }
    return switch_dict.get(value, "Invalid number")
print(switch_demo(2))

# 5. Arrays and Strings
# Python uses lists as arrays
arr = [1, 2, 3, 4, 5]  # List as an array
string_var = "Hello, World!"
print(arr[0], string_var[0])  # Accessing elements

# 6. For Loops
# Iterating over a range of numbers
for i in range(5):
    print("Iteration:", i)

# 7. While Loops
# Looping until a condition is met
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# 8. Functions (Pass by Reference and Value)
def modify_list(lst):
    lst.append(100)  # Modifies original list (Pass by reference)

def modify_value(num):
    num += 10  # Does not modify original variable (Pass by value)
    return num

my_list = [1, 2, 3]
my_num = 10
modify_list(my_list)
my_num = modify_value(my_num)
print(my_list, my_num)

# 9. Time Complexity
# Demonstrating time complexity concepts
import time

def example_function(n):
    start = time.time()
    sum_val = sum(range(n))  # O(n) complexity
    end = time.time()
    print("Execution Time:", end - start)

example_function(1000000)







def switch_fun(value):
    dict = {1 : "Umesh", 2:"himani" , 3:"monali"}
    
    return dict.get(value,"Invalid Entry")


print(switch_fun(3))


