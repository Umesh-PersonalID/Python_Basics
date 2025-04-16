nums = [1,2,3,4,45]
print(nums)


p = nums[4]
print(p)

p2 = nums[-1]
part_of_array = nums[2:]
print(part_of_array)

names = ['navin','kiran']
print(names)



values = [9.5,'navin',25,True]
print(values)

empty_list = []  
single_item_list = [42]  
numbers = [1, 2, 3, 4]  
mixed = ['a', 1, 3.14, True]  
nested = [[1, 2], [3, 4]]  

# Using list() constructor  
from_tuple = list((1, 2, 3))  # [1, 2, 3]  
from_string = list("hello")    # ['h', 'e', 'l', 'l', 'o']  
from_range = list(range(5))    # [0, 1, 2, 3, 4]  


lst = [10, 20, 30, 40, 50]  

# Indexing (O(1) time)  
first = lst[0]    # 10  
last = lst[-1]    # 50  

# Slicing (O(k) time, where k = slice size)  
sub = lst[1:3]    # [20, 30] (start:end-1)  
rev = lst[::-1]   # [50, 40, 30, 20, 10] (reverse)  


lst = [1, 2, 3]  

# Append (O(1) amortized)  
lst.append(4)       # [1, 2, 3, 4]  

# Insert (O(n) time, shifts elements)  
lst.insert(1, 99)   # [1, 99, 2, 3, 4]  

# Extend (O(k), k = len of iterable)  
lst.extend([5, 6])  # [1, 99, 2, 3, 4, 5, 6]  

# Remove (O(n) time, scans list)  
lst.remove(99)      # [1, 2, 3, 4, 5, 6]  

# Pop (O(1) for last, O(n) for middle)  
last = lst.pop()    # 6, list = [1, 2, 3, 4, 5]  
mid = lst.pop(2)    # 3, list = [1, 2, 4, 5]  

# Assign by index (O(1))  
lst[0] = 100        # [100, 2, 4, 5]  

# Clear (O(1))  
lst.clear()         # []  



lst = [1, 2, 2, 3, 4]  

# Count occurrences (O(n))  
print(lst.count(2))  # 2  

# Index of first occurrence (O(n))  
print(lst.index(3))  # 3  

# Reverse in-place (O(n))  
lst.reverse()       # [4, 3, 2, 2, 1]  

# Sort (O(n log n))  
lst.sort()          # [1, 2, 2, 3, 4]  
lst.sort(reverse=True)  # [4, 3, 2, 2, 1]  

# Copy (Shallow copy, O(n))  
copy = lst.copy()   # New list with same elements  


a = [1, 2]  
b = [3, 4]  

# Concatenation (O(n + m))  
combined = a + b    # [1, 2, 3, 4]  

# Repetition (O(n * k))  
repeated = a * 3    # [1, 2, 1, 2, 1, 2]  


lst = [1, 2, 3, 4]  

# Membership (O(n))  
print(3 in lst)      # True  
print(5 not in lst)  # True  

# Length (O(1))  
print(len(lst))      # 4  



# Squares of even numbers (O(n))  
squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]  

# Nested list comprehension  
matrix = [[1, 2], [3, 4]]  
flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4]  



# Unpacking  
first, *_ = [1, 2, 3, 4]  # first=1, rest=[2, 3, 4]  

# Zip (O(min(n, m)))  
names = ["Alice", "Bob"]  
scores = [85, 92]  
zipped = list(zip(names, scores))  # [("Alice", 85), ("Bob", 92)]  

print(zipped[0][0])
# Enumerate (O(n))  
for idx, val in enumerate(["a", "b", "c"]):  
    print(idx, val)  # 0 a, 1 b, 2 c  


# Filter (O(n))  
filtered = list(filter(lambda x: x > 2, [1, 2, 3, 4]))  # [3, 4]
print(filtered)
check = filtered.extend([5,6,7,1,2,3,4,5,6])
print(check)
filtered_extended = filtered + [5,6,7,1,2,3,4,5,6]  # New list
print(filtered)
filtered = list(filter(lambda x:x>2,filtered))
print(filtered)
# Map (O(n))  
mapped = list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]  
print(mapped)
print(min(mapped))
print(sorted(mapped))

mapped.sort(reverse=True)
print(mapped)
