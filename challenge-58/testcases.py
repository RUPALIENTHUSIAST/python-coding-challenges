# testcases.py
from solution import sum_2d_array

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Matrix:", matrix1)
print("Sum:", sum_2d_array(matrix1))  # 21

# Edge Case: Single element
print("\nEdge Case:")
matrix2 = [[10]]
print("Matrix:", matrix2)
print("Sum:", sum_2d_array(matrix2))  # 10

# Negative Case: Invalid element
print("\nNegative Case:")
try:
    matrix3 = [[1, "a"], [3, 4]]
    sum_2d_array(matrix3)
except ValueError as e:
    print("Caught Error:", e)

# Negative Case: Empty matrix
print("\nNegative Case:")
try:
    sum_2d_array([])
except ValueError as e:
    print("Caught Error:", e)
