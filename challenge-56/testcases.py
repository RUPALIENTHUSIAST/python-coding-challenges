# testcases.py

from solution import binary_search

print("Running Binary Search Test Cases...\n")

# Positive Case
arr = [1, 3, 5, 7, 9, 11]
print("Array:", arr)
print("Search 7 → Index:", binary_search(arr, 7))

# Edge Case: First element
print("\nSearch 1 → Index:", binary_search(arr, 1))

# Edge Case: Last element
print("\nSearch 11 → Index:", binary_search(arr, 11))

# Negative Case: Element not present
print("\nSearch 4 → Index:", binary_search(arr, 4))

# Edge Case: Empty array
print("\nEmpty array search → Index:", binary_search([], 10))

# Edge Case: Single element
single = [5]
print("\nSingle element search (5) → Index:", binary_search(single, 5))
print("Single element search (3) → Index:", binary_search(single, 3))
