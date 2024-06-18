#MATRIX

#3.
def sum_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(rows):
        for j in range(cols):
            if i == j:
                main_diagonal_sum += matrix[i][j]
    
    for i in range(rows):
        for j in range(cols):
            if i + j == rows - 1:
                secondary_diagonal_sum += matrix[i][j]
    
    return main_diagonal_sum, secondary_diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_diagonal_sum, secondary_diagonal_sum = sum_diagonal(matrix)

print("Matrix:")
for row in matrix:
    print(row)

print("\nSum of main diagonal:", main_diagonal_sum)
print("Sum of secondary diagonal:", secondary_diagonal_sum)
