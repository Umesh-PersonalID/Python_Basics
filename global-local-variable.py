# ============================================
# ✅ Global Keyword | Global vs Local Variables in Python
# ============================================

# 📌 1. INTRODUCTION:
# - A **local variable** is defined inside a function and can only be used there.
# - A **global variable** is defined outside all functions and is accessible globally.
# - The `global` keyword is used to modify a global variable inside a function.

# --------------------------------------------
# 🔸 2. LOCAL VS GLOBAL VARIABLES
# --------------------------------------------

x = 10  # Global variable

def print_x():
    x = 5  # Local variable (shadows global x)
    print("Inside function (local x):", x)

print_x()
print("Outside function (global x):", x)

# Note: Changing local `x` does NOT affect the global `x`.

# --------------------------------------------
# 🔸 3. USING 'global' TO MODIFY GLOBAL VARIABLES
# --------------------------------------------

counter = 0  # Global variable

def increment():
    global counter  # Declare we're modifying the global variable
    counter += 1
    print("Inside increment(), counter:", counter)

increment()
print("After increment(), counter:", counter)

# --------------------------------------------
# 🔸 4. GLOBAL KEYWORD WITH MULTIPLE FUNCTIONS
# --------------------------------------------

score = 0

def increase():
    global score
    score += 10

def decrease():
    global score
    score -= 5

increase()
decrease()
print("Final score:", score)


# --------------------------------------------
# 🔸 6. ACCESSING GLOBAL VARIABLES WITHOUT MODIFICATION
# --------------------------------------------

name = "Alice"

def say_hello():
    print("Hello", name)  # Can read global variable without using 'global'

say_hello()

# --------------------------------------------
# 🔸 7. BEST PRACTICES AND CAUTIONS
# --------------------------------------------

# ✅ Avoid using too many global variables — they make code harder to debug.
# ✅ Prefer passing variables as function parameters or returning values.
# ✅ Use 'global' only when absolutely needed (e.g., for counters, flags).
# ✅ Use 'nonlocal' in nested functions if you want to modify a variable from the enclosing function.
# ❌ Do NOT use 'global' inside classes to modify attributes — use self.attr instead.

# --------------------------------------------
# 🔸 8. EXAMPLE: BAD PRACTICE VS GOOD PRACTICE
# --------------------------------------------

# ❌ Bad: Using global variable for sum
total = 0

def add_to_total(n):
    global total
    total += n

add_to_total(5)
print("Total:", total)

# ✅ Good: Return and use return value
def add_safe(current_total, n):
    return current_total + n

total = 0
total = add_safe(total, 5)
print("Better Total:", total)

# --------------------------------------------
# 🔸 9. GLOBAL VARIABLE INSIDE A LOOP OR COMPREHENSION
# --------------------------------------------

# Works the same as anywhere else:
count = 0

def count_even(numbers):
    global count
    for num in numbers:
        if num % 2 == 0:
            count += 1

count_even([1, 2, 3, 4, 6])
print("Even count:", count)

# ============================================
# ✅ SUMMARY: KEY DIFFERENCES
# ============================================

# | Feature           | Local Variable           | Global Variable                  |
# |-------------------|---------------------------|----------------------------------|
# | Scope             | Inside function only      | Available throughout file/module |
# | Declaration       | Created inside function   | Created outside any function     |
# | Modify inside fn? | Yes (default behavior)    | No (unless declared global)      |
# | Use global keyword| ❌ Not needed             | ✅ Needed if modifying           |
# | Safe Practice     | ✅ Yes                    | ❌ Avoid if possible             |

# ✅ Use `global` if:
#   - You must modify a global variable inside a function.
#   - It's a script-like situation (e.g., counters, shared flags).
# ✅ Use `nonlocal` if:
#   - You're modifying a variable from an **enclosing function** (not global scope).

# ============================================
# 🔚 End of Global vs Local Variable Tutorial
# ============================================
