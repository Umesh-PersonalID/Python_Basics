"""
=============================
🧵 ITERATORS & GENERATORS
=============================

In Python, **Iterators** and **Generators** are used to iterate over sequences of data — especially useful for large datasets or streams.

"""

# ========== PART 1: ITERATORS ==========

"""
🔹 An *iterator* is any object with:
    - __iter__() → returns the iterator object itself
    - __next__() → returns the next value or raises StopIteration
"""

# Example: manual iterator using `iter()` and `next()`
numbers = [10, 20, 30]
it = iter(numbers)
print(it)
# number_list = list(it)
# print(number_list)

print("Iterator Example:")
print(next(it))  # 10
print(next(it))  # 20
print(next(it))  # 30
# print(next(it))  # ❌ raises StopIteration if uncommented



# Custom iterator by defining a class
class CountDown:
    def __init__(self, start):
        self.num = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        value = self.num
        self.num -= 1
        return value

print("\nCustom Iterator:")
for val in CountDown(5):
    print(val, end=" ")  # 5 4 3 2 1


# ========== PART 2: GENERATORS ==========

"""
🔹 A *generator* is a simpler way to create iterators using `yield` instead of returning all values at once.

    - Generator functions use `yield` to produce values one at a time.
    - Automatically saves state and resumes from where it left off.
"""

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

print("\n\nGenerator Example:")
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # ❌ raises StopIteration if uncommented

# Using generator in a loop
print("\nUsing generator in for loop:")
for num in count_up_to(5):
    print(num, end=" ")  # 1 2 3 4 5


# ========== PART 3: GENERATOR EXPRESSIONS ==========

"""
🔹 Generator expressions are like list comprehensions, but use `()` instead of `[]`
"""

squares = (x * x for x in range(1, 6))  # creates generator object
print("\n\nGenerator Expression:")
for val in squares:
    print(val, end=" ")  # 1 4 9 16 25


# ========== PART 4: MEMORY EFFICIENCY ==========

"""
💡 Generators are memory-efficient — they don’t store the whole list in memory.
"""

import sys

# List comprehension
nums_list = [i for i in range(1000)]
print("\n\nMemory used by list:", sys.getsizeof(nums_list), "bytes")

# Generator expression
nums_gen = (i for i in range(1000))
print("Memory used by generator:", sys.getsizeof(nums_gen), "bytes")


# ========== PART 5: KEY NOTES & BEST PRACTICES ==========

"""
===============================
📝 KEY NOTES AND BEST PRACTICES
===============================

1. ✅ Use `iter()` and `next()` to manually control iteration.
2. ✅ Define `__iter__()` and `__next__()` in custom classes to make them iterable.
3. ✅ Prefer `yield` for complex loops or infinite sequences — cleaner & stateful.
4. ✅ Generators do not store the entire sequence → ideal for large or infinite data.
5. ✅ Generator expressions are great for simple, one-liner iterations.
6. ⚠️ A generator can be iterated only once. Once exhausted, it’s done.
7. ⚠️ Don't mix `next()` with `for` loop unless you're aware of the generator state.

"""

# Example: generator can only be iterated once
gen_once = (x for x in range(3))
print("\nGenerator Exhaustion:")
print(list(gen_once))  # [0, 1, 2]
print(list(gen_once))  # [] ← already exhausted

# Infinite generator
def infinite_counter():
    n = 0
    while True:
        yield n
        n += 1

# Uncomment below to test infinite generator (manual control)
# inf = infinite_counter()
# print(next(inf))  # 0
# print(next(inf))  # 1
# print(next(inf))  # 2

"""
🎯 When to use:
- Use iterators when you need full control over object behavior.
- Use generators for memory-efficient, lazy iteration — especially with large data, streaming, or pipelines.
"""