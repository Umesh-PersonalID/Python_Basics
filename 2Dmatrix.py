# ===============================
# 2D MATRIX IN PYTHON: A SUMMARY
# ===============================

# Creating a 2D matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements using row and column indices
print("Element at row 1, column 2:", matrix[1][2])  # Output: 6

# Dimensions of the matrix
rows = len(matrix)
cols = len(matrix[0])  # assumes all rows are of equal length
print("Matrix dimensions:", rows, "x", cols)

# Iterating through a 2D matrix using nested loops
print("Matrix elements:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=' ')
    print()

# List comprehension to flatten a 2D matrix into 1D
flattened = [val for row in matrix for val in row]
print("Flattened matrix:", flattened)

# Transposing a matrix (rows become columns and vice versa)
transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
print("Transposed matrix:")
for row in transposed:
    print(row)

# Creating a matrix initialized with zeros
zero_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print("Zero matrix:")
for row in zero_matrix:
    print(row)

# Creating a matrix using random integers (requires importing random)
import random
random_matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(3)]
print("Random matrix:")
for row in random_matrix:
    print(row)

# Matrix addition (assuming matrices have same dimensions)
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[A[i][j] + B[i][j] for i in range(len(A))] for j in range(len(A[0]))]
print("Matrix addition result:")
for row in C:
    print(row)

# Matrix multiplication (dot product)
def matrix_multiply(A, B):
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
print("Matrix multiplication result:")
for row in matrix_multiply(A, B):
    print(row)

# Safe access to avoid index errors using try-except
try:
    print(matrix[10][0])  # IndexError expected
except IndexError:
    print("Tried to access out-of-bounds index!")

# Copying a matrix correctly (deep copy)
import copy
original = [[1, 2], [3, 4]]
shallow = original  # changes to 'shallow' will affect 'original'
deep = copy.deepcopy(original)  # independent copy
shallow[0][0] = 99
print("Original after shallow modification:", original)
print("Deep copy remains unchanged:", deep)

# Rotating a matrix 90 degrees clockwise
rotated = [[matrix[rows - j - 1][i] for j in range(rows)] for i in range(cols)]
print("90-degree rotated matrix:")
for row in rotated:
    print(row)

# Search for an element in a matrix (brute force)
def find_element(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return (i, j)
    return (-1, -1)

pos = find_element(matrix, 5)
print("Position of 5 in matrix:", pos)

# Checking if a matrix is symmetric (square and equal to its transpose)
def is_symmetric(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if mat[i][j] != mat[j][i]:
                return False
    return True

sym_matrix = [[1, 2], [2, 1]]
print("Is symmetric matrix:", is_symmetric(sym_matrix))

# End of 2D Matrix Summary in Python
