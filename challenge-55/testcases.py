# testcases.py

from solution import sort_array

print("Running Test Cases...\n")

# Positive Case: Ascending
arr = [5, 2, 9, 1, 7]
print("Original:", arr)
print("Ascending:", sort_array(arr, "asc"))

# Positive Case: Descending
arr = [5, 2, 9, 1, 7]
print("\nOriginal:", arr)
print("Descending:", sort_array(arr, "desc"))

# Edge Case: Single element
arr = [10]
print("\nSingle element array:", arr)
print("Ascending:", sort_array(arr, "asc"))

# Edge Case: Empty array
arr = []
print("\nEmpty array:", arr)
print("Ascending:", sort_array(arr, "asc"))

# Negative Case: Invalid order
try:
    arr = [1, 2, 3]
    sort_array(arr, "up")
except ValueError as e:
    print("\nCaught Error for invalid order:", e)
