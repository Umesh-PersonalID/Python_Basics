# ============================================
# 🔁 PYTHON RECURSION - FULL TUTORIAL
# ============================================

# ------------------------------------------------
# 1. WHAT IS RECURSION?
# ------------------------------------------------
# Recursion is when a function calls itself to solve smaller subproblems.
# It is often used in divide-and-conquer algorithms, trees, graphs, backtracking, etc.



# 🔁 Every recursive function must have:
# - A **base case** to stop recursion
# - A **recursive case** to break the problem down

# ------------------------------------------------
# 2. BASIC EXAMPLE - Factorial
# ------------------------------------------------
def factorial(n):
    """Returns n! using recursion"""
    if n == 0 or n == 1:          # Base case
        return 1
    return n * factorial(n - 1)   # Recursive case

print("Factorial of 5:", factorial(5))  # Output: 120

# ------------------------------------------------
# 3. ANOTHER EXAMPLE - Fibonacci
# ------------------------------------------------
def fibonacci(n):
    """Returns the nth Fibonacci number (inefficient)"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci(6):", fibonacci(6))  # Output: 8

# ⚠️ Note: This version is exponential in time (O(2^n))!

# ------------------------------------------------
# 4. OPTIMIZATION - MEMOIZATION (Top-Down)
# ------------------------------------------------
# Use functools.lru_cache to cache results and speed up recursion
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

print("Fibonacci with memoization:", fib_memo(30))  # Much faster!

# ------------------------------------------------
# 5. TAIL RECURSION (Python doesn’t optimize it)
# ------------------------------------------------
# Tail recursion is when the recursive call is the last operation.
# Python doesn’t optimize tail calls, so deep recursion can cause stack overflow.

# Tail-recursive factorial:
def tail_factorial(n, acc=1):
    if n == 0:
        return acc
    return tail_factorial(n - 1, acc * n)

print("Tail-recursive factorial of 5:", tail_factorial(5))

# ------------------------------------------------
# 6. TREE TRAVERSAL (Classic Recursion Use-Case)
# ------------------------------------------------
# Example of in-order traversal in binary tree

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        in_order(root.right)

# Sample Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("\nIn-order Traversal:")
in_order(root)  # Output: 4 2 1 3

# ------------------------------------------------
# 7. BACKTRACKING EXAMPLE - Generating Combinations
# ------------------------------------------------
def generate_combinations(slate, i, arr):
    if i == len(arr):
        print("".join(slate))
        return
    # Include current element
    slate.append(arr[i])
    generate_combinations(slate, i + 1, arr)
    slate.pop()  # backtrack
    # Exclude current element
    generate_combinations(slate, i + 1, arr)

print("\nCombinations of 'abc':")
generate_combinations([], 0, list("abc"))

# ------------------------------------------------
# 8. HELPER METHOD PATTERN
# ------------------------------------------------
# Useful for recursion problems that need extra parameters

def is_palindrome(s):
    def helper(l, r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return helper(l + 1, r - 1)
    
    return helper(0, len(s) - 1)

print("\nIs 'racecar' a palindrome?", is_palindrome("racecar"))  # True

# ------------------------------------------------
# 9. KEY TIPS & CAVEATS
# ------------------------------------------------
# ✅ Always define a base case to avoid infinite recursion.
# ✅ Python has a recursion depth limit (~1000 by default):

import sys
print("\nRecursion limit:", sys.getrecursionlimit())

# You can change it (not recommended unless necessary)
# sys.setrecursionlimit(2000)

# ✅ Use memoization or convert to iteration when performance is an issue.
# ✅ Debug recursively with print statements or use visual tools (e.g., Python Tutor).
# ✅ Recursion is elegant but not always the most efficient for large inputs.

# ------------------------------------------------
# 10. RECURSION VS ITERATION
# ------------------------------------------------
# Many recursive algorithms can be written iteratively.
# Example: factorial (iterative version)

def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print("Iterative factorial:", factorial_iter(5))

# ------------------------------------------------
# ✅ SUMMARY
# ------------------------------------------------
# - Recursion solves problems by dividing them into smaller versions of themselves.
# - Needs a base case and a recursive case.
# - Can be slow without memoization.
# - Excellent for tree/graph problems, combinatorics, and divide & conquer.
# - Watch out for recursion depth and use memoization/tail recursion wisely.



#Reverse the array using recursion

l1 = [1,2,3,4,5,6,7,8,9]

n = len(l1)-1
def fun(n,i):
    if i < n//2:
        return
    l1[i],l1[n-i] = l1[n-i],l1[i]
    fun(n,i-1)
    return 

fun(n,n)
print(l1)