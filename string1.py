s = "Python"

# Length
print(len(s))        # 6 → O(1) time (stores length)

# Concatenation
print(s + " Rocks")  # Python Rocks → O(n+m) time

# Repetition
print(s * 3)         # PythonPythonPython → O(n*k) time

# Indexing
print(s[0])          # 'P' → O(1) time
print(s[-1])         # 'n' (last char)

# Slicing
print(s[1:4])        # 'yth' → O(k) for slice of size k
print(s[::-1])       # 'nohtyP' (reverse)

### IMPORTANT:
# - Negative indices count from end
# - Slicing never raises IndexError


s = "  PyThoN  "

print(s.lower())     # '  python  ' → O(n)
print(s.upper())     # '  PYTHON  ' → O(n)
print(s.title())     # '  Python  ' → O(n)
print(s.swapcase())  # '  pYtHOn  ' → O(n)
print(s.capitalize())# '  python  ' → O(n)

### IMPORTANT:
# - Original string unchanged (strings are immutable)
# - Case conversion depends on locale settings



s = "Hello World"

# Find/index
print(s.find('o'))      # 4 → O(n) (returns -1 if not found)
print(s.index('o'))     # 4 → O(n) (raises ValueError if not found)
print(s.rfind('o'))     # 7 (search from right)

# Count occurrences
print(s.count('l'))     # 3 → O(n)

# Validation
print(s.startswith('H'))# True → O(k) for prefix of length k
print(s.endswith('d'))  # True → O(k)
print('123'.isdigit())  # True
print('abc'.isalpha())  # True
print('a1'.isalnum())   # True
print(' '.isspace())  # True

### IMPORTANT:
# - find() vs index(): prefer find() to avoid exceptions
# - Validation methods useful for input checking


s = "Python Programming"

# Replace
print(s.replace('P', 'J',1))  # 'Jython Jrogramming' → O(n)

# Split
print(s.split())           # ['Python', 'Programming'] → O(n)
print("a,b,c".split(','))  # ['a', 'b', 'c']

# Join
print('-'.join(['a', 'b']))# 'a-b' → O(n) for n elements

# Strip whitespace
print("  hi  ".strip())    # 'hi' → O(n)

# Partition
print(s.partition(' '))    # ('Python', ' ', 'Programming')

### IMPORTANT:
# - replace() can take count param: s.replace('n', 'x', 1)
# - join() is fastest way to concatenate many strings


# String interning (some strings cached)
a = "hello"
b = "hello"
print(id(a))
print(id(b))
print(a is b)  # True (may be interned)

c = "hello world is lakhan"
d = "hello world is lakhan"
print(c is d)  # False (longer strings usually not interned)

### IMPORTANT:
# 

# - Python may intern small strings (memory opt
# imization)
# - Don't rely on 'is' for string comparison, use '=='



def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n - 2) 


n = 20 # This means summing from 0 to 7
fibo(n)
print(fibo(n))  # 6765 (20th Fibonacci number)

def ncr(n,r):
    global i 
    if r == 1:
        return n
    i+=1
    return ncr(n-1,r-1)*(n/r)

n = 6
r = 3
print(ncr(n,r))  # 20 (6 choose 3)