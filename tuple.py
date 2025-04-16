tup = (1,34,2,3,45)

print(tup[3])
print(tup[2])

print(tup.index(34))

#Iteration in tuple faster in tuple

# We can not change the value of element in tuple


empty_tuple = ()
single_item_tuple = (42,)  # Note the comma for single-item tuples
print(type(single_item_tuple))
numbers = (1, 2, 3, 4)
mixed = ('a', 1, 3.14, True)

t = (10, 20, 30, 40, 50)

# Indexing
print(t[0])     # 10 (first element)
print(t[-1])    # 50 (last element)

# Slicing
print(t[1:3])   # (20, 30)
print(t[:2])    # (10, 20)
print(t[2:])    # (30, 40, 50)
p = t[::-1]  # (50, 40, 30, 20, 10) - reverse
print(p)


t = (1, 2, 3, 2, 4, 2)

# count() - counts occurrences of a value
print(t.count(2))  # 3

# index() - returns first index of a value
print(t.index(3))  # 2
print(t.index(2))  # 1 (first occurrence)



t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
combined = t1 + t2  # (1, 2, 3, 4, 5, 6)

# Repetition
repeated = t1 * 3   # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership testing
print(2 in t1)      # True
print(7 not in t1)  # True

# Length
print(len(t1))      # 3

# Iteration
for item in t1:
    print(item)

# Packing
t = 1, 2, 3  # Parentheses optional in many cases

# Unpacking
a, b, c = t   # a=1, b=2, c=3

# Extended unpacking (Python 3+)
first, *rest = t  # first=1, rest=[2, 3]


print((1, 2, 3) < (1, 2, 4))  # True (lexicographical comparison)
print((1, 2) < (1, 2, -1))    # True
print((1, 3) > (1, 2))        # True


lst = [1, 2, 3]
t = tuple(lst)      # Convert list to tuple

s = "hello"
t = tuple(s)        # ('h', 'e', 'l', 'l', 'o')
print(t)


t = (5, 2, 8, 1, 9)

print(min(t))       # 1
print(max(t))       # 9
print(sum(t))       # 25
print(sorted(t))    # [1, 2, 5, 8, 9] (returns a list)
