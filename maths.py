import numpy as np


# integer division
# single division will always give you the float number
c = 5 // 2 
print(c)    
print('navin\'s laptop \n')

# \n is break line

# Absolute value
abs(-5.5)       # 5.5 → __abs__

# Rounding
round(3.14159, 2)  # 3.14
import math
math.floor(3.7)    # 3
math.ceil(3.2)     # 4

# Divmod (quotient and remainder)
quot, rem = divmod(10, 3)  # (3, 1)

### IMPORTANT:
# - round() uses "banker's rounding" (rounds to nearest even)
# - floor() and ceil() return floats for float inputs
# - divmod() is faster than separate // and % operations


# Power functions
pow(2, 3)         # 8 (2**3)
math.exp(1)       # e^1 ≈ 2.718
math.sqrt(16)     # 4.0

# Logarithmic functions
print(math.log(10)) # 2.0 (log₁₀100)
math.log2(8)      # 3.0
math.log10(1000)  # 3.0

### IMPORTANT:
# - math.sqrt() is faster than **0.5 for small numbers
# - Natural log (base e) is default for math.log()
x =math.pow(3,4)
print(x)
print(math.log(math.e))
import random

# Basic random numbers
print(random.random())          # [0.0, 1.0)
print(random.uniform(1, 10) )  # Float in [1,10]
print(random.randint(1, 6))    # Int in [1,6]

# Sequences
random.choice(['a','b','c'])  # Pick one
print(random.sample(range(100), 5))  # 5 unique numbers

### IMPORTANT:
# - Uses Mersenne Twister PRNG internally
# - For cryptography, use secrets module instead
# - seed() for reproducible results