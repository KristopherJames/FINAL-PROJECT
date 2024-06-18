#MATRIX

#1.
def transpose_matrix(matrix):
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = transpose_matrix(matrix)

for row in transposed:
    print("[", end="")
    for i in range(len(row)):
        print(row[i], end="")
        if i < len(row) - 1:
            print(",", end="")
    print("]")
