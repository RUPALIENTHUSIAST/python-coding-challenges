# testcases.py

from solution import sum_of_array

print("Running Test Cases...\n")

# Test Case 1: Normal case
print("Test Case 1:")
print(sum_of_array([1, 2, 3, 4, 5]))  # Expected: 15

# Test Case 2: Single element
print("\nTest Case 2:")
print(sum_of_array([10]))  # Expected: 10

# Test Case 3: Empty array
print("\nTest Case 3:")
print(sum_of_array([]))  # Expected: 0

# Test Case 4: Float values
print("\nTest Case 4:")
print(sum_of_array([1.5, 2.5, 3]))  # Expected: 7.0

# Test Case 5: Invalid element
print("\nTest Case 5:")
try:
    print(sum_of_array([1, "a", 3]))
except ValueError as e:
    print("Caught Error:", e)
