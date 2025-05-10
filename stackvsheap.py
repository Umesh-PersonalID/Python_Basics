"""
===========================
📚 STACK vs HEAP in Python
===========================

In Python, memory is divided into two main regions:
    - 🥞 Stack Memory: for function calls and local variables.
    - 🧠 Heap Memory: for dynamic (object) allocation.

⚠️ NOTE: Python manages memory differently than low-level languages like C/C++.
Everything in Python is an object, and most data lives on the heap.
"""

# ========== PART 1: STACK MEMORY ==========

def stack_example():
    # Local variables are stored in stack memory
    x = 10
    y = 20
    result = x + y  # This result is also a local variable
    return result  # All of these are popped off the stack after function returns

print("Stack Example Result:", stack_example())

# Call stack example (recursive function)
def factorial(n):
    # Each call creates a new stack frame with its own `n`
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial(5) using stack recursion:", factorial(5))


# ========== PART 2: HEAP MEMORY ==========

# Objects like lists, dicts, and classes are stored in the heap.
a = [1, 2, 3]
b = a  # `b` points to the same list object in heap
a.append(4)

print("\nHeap Example:")
print("a:", a)  # [1, 2, 3, 4]
print("b (shares reference):", b)  # [1, 2, 3, 4]


# ========== PART 3: IDENTITY & REFERENCES ==========

x = 500
y = 500
print("\nInteger Interning (Heap vs Stack nuance):")
print("x == y:", x == y)  # True (value check)
print("x is y:", x is y)  # May be True or False (identity check — points to same object?)

# Immutable objects like integers, strings may be interned
s1 = "hello"
s2 = "hello"
print("s1 is s2 (interned strings):", s1 is s2)  # Likely True

# Mutable objects always live in heap
list1 = [1, 2]
list2 = [1, 2]
print("list1 is list2 (mutable objects):", list1 is list2)  # False


# ========== PART 4: FUNCTIONS, OBJECTS, and the HEAP ==========

class Student:
    def __init__(self, name):
        self.name = name  # `self` is stored on heap

s = Student("Umesh")
print("\nStudent object stored on heap. Name:", s.name)


# ========== PART 5: GARBAGE COLLECTION & MEMORY MANAGEMENT ==========

import sys
import gc

# Example of reference counting
print("\nReference Counting:")
obj = [1, 2, 3]
print("Initial refcount:", sys.getrefcount(obj))  # Includes local reference in getrefcount()
alias = obj
print("After aliasing:", sys.getrefcount(obj))

# For circular references, Python uses garbage collector
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a  # Circular reference

# Forcibly collect garbage
del a
del b
gc.collect()
print("Garbage collector used for cyclic references.")

# ========== PART 6: STACK LIMITS ==========

import sys

print("\nStack Recursion Limit:")
print("Recursion limit:", sys.getrecursionlimit())

# Uncomment below to test stack overflow
# def recurse_forever():
#     return recurse_forever()
# recurse_forever()  # Will crash with RecursionError

"""
==============================
💡 KEY NOTES & BEST PRACTICES
==============================

1. ✅ Stack memory:
   - Fast, used for function calls, parameters, local variables.
   - Automatically managed (frame created/popped with calls/returns).
   - Limited size → Recursion too deep causes RecursionError.

2. ✅ Heap memory:
   - Slower, stores objects (lists, dicts, custom classes).
   - Managed by Python using reference counting + garbage collection.
   - Mutable objects are always heap-allocated.

3. ⚠️ `is` vs `==`:
   - `is` checks identity (same object in memory).
   - `==` checks value equality.

4. ⚠️ Memory leaks:
   - Rare in Python, but can occur with circular references if `__del__` is badly implemented.
   - Use `gc.collect()` to force cleanup or investigate issues.

5. ✅ Debugging memory:
   - Use `sys.getrefcount()` to inspect reference count.
   - Use `gc` module for garbage collection insight.

6. 📌 Immutable objects like integers and strings may be **interned** (reused in memory).
   - Don’t rely on `is` for such comparisons in production code.

7. 💡 Everything in Python (even `int`) is an object — so most data lives in the heap.
   - But variable references (names) and stack frames are managed using stack memory.
"""

