#MATRIX

#2.
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

row_sums = np.sum(matrix, axis=1)

col_sums = np.sum(matrix, axis=0)

print("Matrix:")
print(matrix)
print("\nSum of rows:")
print(row_sums)
print("\nSum of columns:")
print(col_sums)
