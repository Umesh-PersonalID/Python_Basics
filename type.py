# Integers (unlimited precision)
x = 42          # int
y = -1000000    # Still int
print(type(10**100))  # <class 'int'> (handles arbitrarily large numbers)

# Floats (64-bit double precision)
pi = 3.14159    # float
sci = 2.5e-4    # 0.00025 (scientific notation)

# Complex numbers
z = 3 + 4j      # <class 'complex'>
print(z.real)    # 3.0
print(z.imag)    # 4.0

# Boolean (subclass of int)
is_valid = True  # <class 'bool'> (True=1, False=0)

# IMPORTANT:
# - Arithmetic ops: +, -, *, /, // (floor div), % (mod), ** (power)
# - int division (/) always returns float in Python 3
# - Use decimal.Decimal for precise financial calculations




s = "Hello"      # <class 'str'>
s2 = 'World'     # Single or double quotes
multi = """This
is multi-line"""

# Key Operations:
print(len(s))            # 5 (O(1))
print("ell" in s)        # True (O(n) substring search)
print(s + " " + s2)      # Concatenation (O(n+m))
print(s * 3)             # Repetition (O(n*k))
print(s[1:4])            # Slicing (O(k)) -> 'ell'

# IMPORTANT:
# - Immutable (can't modify after creation)
# - str.join() is fastest for concatenating many strings
# - f-strings (Python 3.6+) best for formatting: f"Value: {x}"
# - Internally uses UTF-8 or UTF-16 (depending on content)



lst = [1, "two", 3.0]  # <class 'list'>
lst[1] = 2             # Mutable (can modify elements)

# Key Operations:
lst.append(4)          # O(1) amortized
lst.insert(0, 0)       # O(n) (shifts elements)
lst.extend([5,6])      # O(k) for k extensions
x = lst.pop()          # O(1) (last element)
y = lst.pop(0)         # O(n) (first element)

# IMPORTANT:
# - Dynamic array implementation
# - Slicing creates new list (shallow copy)
# - List comprehensions faster than loops for transformations


t = (1, "two", 3.0)   # <class 'tuple'>
single = (42,)         # Note comma for single-element

# Key Operations:
print(t[1])           # 'two' (O(1) access)
print(t + (4,5))      # Concatenation (O(n+m))
print(t * 2)          # Repetition (O(n*k))

# IMPORTANT:
# - Immutable (hashable if all elements are hashable)
# - Faster than lists for fixed data
# - Used as dict keys when containing immutable types



d = {"name": "Alice", "age": 30}  # <class 'dict'>

# Key Operations:
d["city"] = "NY"     # O(1) avg insert
val = d["name"]      # O(1) avg lookup
del d["age"]         # O(1) avg delete

# IMPORTANT:
# - Hash table implementation (keys must be hashable)
# - Preserves insertion order (Python 3.7+)
# - Average O(1) for lookup/insert/delete
# - Worst case O(n) if many hash collisions



s = {1, 2, 3}        # <class 'set'>
fs = frozenset(s)    # Immutable version

# Key Operations:
s.add(4)             # O(1) avg
s.remove(2)          # O(1) avg
print(3 in s)        # O(1) membership test

# IMPORTANT:
# - Hash table implementation (only stores keys)
# - Elements must be hashable
# - Union/intersection ops: |, &, -, ^



# None Type
x = None             # <class 'NoneType'>
#X is not assign to any value

# Ellipsis (...)
y = ...              # Used in NumPy and type hints

# Functions/Classes
def f(): pass
print(type(f))       # <class 'function'>

# IMPORTANT:
# - None is singleton (only one instance exists)
# - Used as default return value for functions



# Explicit conversion
int("42")            # 42
float(3)             # 3.0
str(123)             # "123"
list("abc")          # ['a', 'b', 'c']
tuple([1,2,3])       # (1, 2, 3)
set([1,1,2])         # {1, 2}

# IMPORTANT:
# - Implicit conversion happens in operations (e.g., int + float → float)
# - May raise ValueError if conversion not possible

num = 435263422
lst2 = str(num)[::-1]
print(int(lst2))



p = 3
k = 6
comp = complex(p,k)
print(comp)