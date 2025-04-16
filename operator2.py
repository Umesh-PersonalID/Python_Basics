import math

#Arithmetic Operators


# Basic operations
print(5 + 3)    # 8 (__add__)
print(5 - 3)    # 2 (__sub__)
print(5 * 3)    # 15 (__mul__)
print(5 / 2)    # 2.5 (__truediv__) - ALWAYS returns float
print(5 // 2)   # 2 (__floordiv__) - integer division
print(5 % 2)    # 1 (__mod__) - remainder
print(5 ** 3)   # 125 (__pow__) - exponentiation

# Special cases
print(-5.5)     # -5.5 (__neg__)
print(+5)       # 5 (__pos__)
print(abs(-5))  # 5 (__abs__)

# IMPORTANT:
# - For custom classes, implement magic methods (__add__, etc.)
# - Division (/) always returns float in Python 3
# - ** has higher precedence than - (so -2**2 = -4)




#Comparison Operators


# Standard comparisons (return bool)
print(5 == 5)   # True (__eq__)
print(5 != 3)   # True (__ne__)
print(5 > 3)    # True (__gt__)
print(5 < 3)    # False (__lt__)
print(5 >= 5)   # True (__ge__)
print(5 <= 3)   # False (__le__)

# Chained comparisons
print(1 < 2 <= 3)  # True (equivalent to 1 < 2 and 2 <= 3)

# IMPORTANT:
# - Works with all comparable types (int, float, str, etc.)
# - For custom classes, implement comparison magic methods
# - is vs ==: 'is' checks identity (memory address), == checks equality


# Logical Operators


# Boolean operations
print(True and False)  # False (short-circuit eval)
print(True or False)   # True (short-circuit eval)
print(not True)        # False

# Truthy/Falsy evaluation
print(0 or "defat")  # "default" (0 is Falsy)
print([] and 5)        # [] (empty list is Falsy)

if [] or "Umesh":
    print("I am in")

# IMPORTANT:
# - Short-circuit: right operand not evaluated if result known from left
# - Falsy values: False, 0, "", [], (), {}, None
# - and returns last evaluated operand, or returns first truthy operand


#BitWise Operator
# Binary operations
print(5 & 3)   # 1 (AND) - 0101 & 0011 = 0001
print(5 | 3)   # 7 (OR)  - 0101 | 0011 = 0111
print(5 ^ 3)   # 6 (XOR) - 0101 ^ 0011 = 0110
print(~5)      # -6 (NOT) - two's complement
print(5 << 1)  # 10 (left shift) - 0101 -> 1010
print(5 >> 1)  # 2 (right shift) - 0101 -> 0010

# IMPORTANT:
# - Works on integers (converts to binary)
# - ~x = -x - 1 (two's complement)
# - Used in low-level programming, hashing algorithms


