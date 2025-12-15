# testcases.py

from solution import transpose_matrix

print("Running Test Cases...\n")

# Positive Case
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrix:")
print(matrix1)
print("Transpose:")
print(transpose_matrix(matrix1))

# Edge Case (1x1 matrix)
matrix2 = [[10]]
print("\nMatrix:")
print(matrix2)
print("Transpose:")
print(transpose_matrix(matrix2))

# Edge Case (single row)
matrix3 = [[1, 2, 3, 4]]
print("\nMatrix:")
print(matrix3)
print("Transpose:")
print(transpose_matrix(matrix3))
