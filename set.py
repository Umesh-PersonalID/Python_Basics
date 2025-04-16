s = {22,25,4,21,5,5,4,98}

#set is using the concept of hash
# we want to fatch the element as fast as possible
#Remove duplicates

#Indexing is not supported
# print(s[2])
print(s)

s.update({123,23,4,5454})
print(s)

s.add(76)
print(s)


empty_set = set()          # {} creates an empty dictionary, not set
numbers = {1, 2, 3, 4}
mixed = {'a', 1, 3.14, True}
from_list = set([1, 2, 2, 3])  # {1, 2, 3} - duplicates removed



s = {1, 2, 3}

# Add elements
s.add(4)            # {1, 2, 3, 4}
s.add(2)            # No change (duplicates not allowed)

# Remove elements
s.remove(2)         # {1, 3, 4} - raises KeyError if not found
s.discard(5)        # No error if element not found
popped = s.pop()    # Removes and returns arbitrary element
print(popped)
# Clear set
s.clear()           # set() 



a = {1, 2, 3}
b = {2, 3, 4}

# Union
print(a.union(b))           # {1, 2, 3, 4}
print(a | b)                # Same with operator

# Intersection
print(a.intersection(b))    # {2, 3}
print(a & b)                # Same with operator

# Difference
print(a.difference(b))      # {1}
print(a - b)                # Same with operator

# Symmetric Difference (elements in either but not both)
print(a.symmetric_difference(b))  # {1, 4}
print(a ^ b)                      # Same with operator


x = {1, 2}
y = {1, 2, 3}

# Subset
print(x.issubset(y))        # True
print(x <= y)               # True
print(x < y)                # True (proper subset)

# Superset
print(y.issuperset(x))      # True
print(y >= x)               # True
print(y > x)                # True (proper superset)

# Disjoint (no common elements)
print(x.isdisjoint({4, 5})) # True


s = {1, 2, 3}

# Length
print(len(s))               # 3

# Membership testing
print(2 in s)               # True o(1)
print(5 not in s)           # True o(1)

# Update operations (modify set in-place)
s.update([3, 4, 5])         # {1, 2, 3, 4, 5}
s.intersection_update({2, 3, 6})  # {2, 3}
s.difference_update({2})    # {3}
s.symmetric_difference_update({3, 4})  # {4}


squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
even_squares = {x**2 for x in range(10) if x % 2 == 0}  # {0, 4, 16, 36, 64}


lst = [1, 2, 2, 3]
s = set(lst)            # Convert list to set {1, 2, 3}

t = (1, 2, 2, 3)
s = set(t)              # Convert tuple to set {1, 2, 3}

s = set("hello")        # {'h', 'e', 'l', 'o'} (unordered, unique)

