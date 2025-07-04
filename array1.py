arr = [10, 20, 30, 40]
print("Array:", arr)

#array similar to list, but all value of same type. 
# Access elements
print("First element:", arr[0])

# Modify element
arr[1] = 5
print("Modified array:", arr)

# Append new element
arr.append(50)
print("After append:", arr)

# Insert at specific index
arr.insert(2, 100)
print("After insert at index 2:", arr)

# Delete element by index
del arr[3]
print("After deleting index 3:", arr)

# Remove specific value
arr.remove(100)
print("After removing 100:", arr)

#will return error is value is not present


# Slicing (subarray)
print("Sliced array [1:3]:", arr[1:3])

# Length of array
print("Length:", len(arr))

# Loop through array
for element in arr:
    print("Element:", element)

# Check if value exists
if 25 in arr:
    print("25 is in array")

# List comprehension (square of elements)
squares = [x*x for x in arr]
print("Squares:", squares)

sqr =  [x**2 for x in range(0,14)]
print(sqr)

import numpy as np

# Create a NumPy array
np_array = np.array([1, 2, 3, 4])
print("NumPy array:", np_array)

# Element-wise operations
print("Array * 2:", np_array * 2)

# Shape and size
print("Shape:", np_array.shape)
print("Size:", np_array.size)

my_array = [1,2,3,4,1,2,3,2,3,45,3,4,5,6,8,5,4,6,7,5]
x = int(input("Enter value you wanna get index"))

for i in range(len(my_array)):
    if my_array[i] == x:
        print(i)
        break
    
    
    
m = np.matrix('1 2 4;3 4 2;3 4 52; 4 4 2 ;2 4 3')
print(m)
print(m.max())

m1 = np.matrix('1 2 4;3 4 2;3 4 3')
m2  = np.matrix('1 2 4;3 3 2;3 4 5')
print(m1*m2)