# testcases.py

from solution import reverse_array

print("Running Test Cases...\n")

# Positive Case
arr = [1, 2, 3, 4, 5]
print("Original:", arr)
print("Reversed:", reverse_array(arr))

# Edge Case: Single element
arr = [10]
print("\nSingle element array:", arr)
print("Reversed:", reverse_array(arr))

# Edge Case: Empty array
arr = []
print("\nEmpty array:", arr)
print("Reversed:", reverse_array(arr))

# Negative Case: Negative numbers
arr = [-1, -2, -3, -4]
print("\nArray with negative numbers:", arr)
print("Reversed:", reverse_array(arr))
