from solution import create_2d_array, display_row_wise

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
matrix = create_2d_array(2, 3, [1, 2, 3, 4, 5, 6])
display_row_wise(matrix)

# Edge Case
print("\nEdge Case (1x1 matrix):")
matrix = create_2d_array(1, 1, [10])
display_row_wise(matrix)

# Negative Case
print("\nNegative Case:")
try:
    create_2d_array(2, 2, [1, 2, 3])
except ValueError as e:
    print("Caught Error:", e)
