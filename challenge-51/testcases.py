# testcases.py

from solution import search_element

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
arr1 = [5, 3, 9, 1, 7]
print("Array:", arr1, "Search 9 → Index:", search_element(arr1, 9))   # 2
print("Array:", arr1, "Search 5 → Index:", search_element(arr1, 5))   # 0

# Edge Cases
print("\nEdge Cases:")
arr2 = [0, 0, 0]
print("Array:", arr2, "Search 0 → Index:", search_element(arr2, 0))   # 0
arr3 = [-5, -10, 0]
print("Array:", arr3, "Search -10 → Index:", search_element(arr3, -10))  # 1
arr4 = [42]
print("Array:", arr4, "Search 42 → Index:", search_element(arr4, 42))    # 0

# Negative Case
print("\nNegative Case:")
arr5 = [1, 2, 3]
print("Array:", arr5, "Search 10 → Index:", search_element(arr5, 10))    # -1
