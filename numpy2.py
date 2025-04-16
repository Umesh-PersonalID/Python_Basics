#6 ways to create array using numpy

"""1. array()
2. linspace()
3. logspace()
4. arange()
5. zeros()
6. ones()"""


# ========================================
# ✅ NumPy: Complete Revision for Intermediates
# ========================================

# 📌 1. INTRODUCTION:
# NumPy (Numerical Python) is the foundation of numerical computing in Python.
# It provides a powerful N-dimensional array object and tools for performing operations on these arrays.
# Efficient, vectorized, and great for math, stats, ML, and image processing.

import numpy as np

# ----------------------------------------
# 🔸 2. ARRAY CREATION
# ----------------------------------------

# From Python list
arr1 = np.array([1, 2, 3])
print("1D Array:", arr1)

# 2D Array
arr2 = np.array([[1, 2], [3, 4]])
print("2D Array:\n", arr2)

# Create arrays of zeros, ones, or a constant
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
full = np.full((2, 2), 7)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Full:\n", full)

# Identity Matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# Random values
rand = np.random.rand(2, 2)
rand_int = np.random.randint(0, 10, (2, 3))
print("Random Float Array:\n", rand)
print("Random Int Array:\n", rand_int)

# Sequential arrays
seq = np.arange(0, 10, 4)  # step of 2  #will give int
linspace = np.linspace(0, 1, 5)  # 5 evenly spaced numbers from 0 to 1
print("Arange:", seq)
print("Linspace:", linspace)

# ----------------------------------------
# 🔸 3. ARRAY ATTRIBUTES
# ----------------------------------------

print("Shape:", arr2.shape)
print("Size:", arr2.size)
print("Data type:", arr2.dtype)
print("Dimensions:", arr2.ndim)

# ----------------------------------------
# 🔸 4. ARRAY INDEXING AND SLICING
# ----------------------------------------

a = np.array([[1, 2, 3], [4, 5, 6]])
print("Element at row 1, col 2:", a[1, 2])  # → 6

# Slicing: [row_start:row_end, col_start:col_end]
print("Slice of array:\n", a[0:2, 1:3])

# Fancy indexing
fancy = a[[0, 1], [1, 2]]  # Picks (0,1) and (1,2)
print("Fancy indexing result:", fancy)

# Boolean indexing
bool_idx = a > 3
print("Elements > 3:", a[bool_idx])

# ----------------------------------------
# 🔸 5. ARRAY OPERATIONS
# ----------------------------------------

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Element-wise operations
print("Addition:", x + y)
print("Multiplication:", x * y)
print("Power:", x ** 2)

# Aggregate functions
print("Mean:", x.mean())
print("Sum:", x.sum())
print("Standard Deviation:", x.std())
print("Max/Min:", x.max(), x.min())
print("Argmax:", x.argmax())

# Matrix operations
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print("Matrix Product:\n", np.dot(mat1, mat2))  # or mat1 @ mat2
print("Transpose:\n", mat1.T)

# ----------------------------------------
# 🔸 6. RESHAPING AND FLATTENING
# ----------------------------------------

reshaped = np.arange(15).reshape(3, 5)
print("Reshaped (3x5):\n", reshaped)

flattened = reshaped.flatten()
print("Flattened:\n", flattened)

# Stacking arrays
vstack = np.vstack((x, y))
hstack = np.hstack((x, y))
print("Vertical Stack:\n", vstack)
print("Horizontal Stack:\n", hstack)

# ----------------------------------------
# 🔸 7. BROADCASTING
# ----------------------------------------

# Smaller shape array auto-expands to match larger array
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30])
broadcasted = a + b  # (3x1) + (3,) => (3x3)
print("Broadcasted Result:\n", broadcasted)

# ----------------------------------------
# 🔸 8. COPYING VS VIEWING
# ----------------------------------------

arr = np.array([1, 2, 3])
view = arr[:]
copy = arr.copy()

arr[0] = 100
print("Original Modified:", arr)
print("View (linked):", view)
print("Copy (independent):", copy)

# ----------------------------------------
# 🔸 9. HANDLING NAN AND INF
# ----------------------------------------

nan_arr = np.array([1, np.nan, 2, np.nan])
print("Mean ignoring NaNs:", np.nanmean(nan_arr))  # Use nan-safe functions

# ----------------------------------------
# 🔸 10. SAVING / LOADING ARRAYS
# ----------------------------------------

# Save to .npy file
np.save("my_array.npy", arr1)

# Load from .npy
loaded = np.load("my_array.npy")
print("Loaded array:", loaded)

# ----------------------------------------
# 🔸 11. NUMPY TIPS & CAVEATS
# ----------------------------------------

# ✅ Use NumPy for vectorized operations — it's faster than for-loops.
# ✅ Broadcasting rules make code cleaner — but watch out for unexpected shapes.
# ❗ Avoid chained assignments: arr[arr > 0] = x is OK; arr[arr > 0][0] = x is not!
# ✅ Use `.copy()` if you want to avoid modifying the original array.

# ========================================
# 🔚 Done! You’ve revised NumPy essentials.
# ========================================
  