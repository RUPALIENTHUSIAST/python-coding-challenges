from solution import element_exists

print("Running Test Cases...\n")

# Positive Case
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Test 1:", element_exists(matrix1, 5))  # True

# Negative Case
print("Test 2:", element_exists(matrix1, 10))  # False

# Edge Case: Single element
matrix2 = [[7]]
print("Test 3:", element_exists(matrix2, 7))  # True

# Edge Case: Empty matrix
try:
    element_exists([], 3)
except ValueError as e:
    print("Test 4 (Edge):", e)
