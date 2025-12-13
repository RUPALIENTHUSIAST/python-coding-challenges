# testcases.py

from solution import count_odd_even

print("Running Test Cases...\n")

# Positive Case
arr1 = [1, 2, 3, 4, 5, 6]
odd_count, even_count = count_odd_even(arr1)
print("Array:", arr1)
print("Odd Count:", odd_count)   # 3
print("Even Count:", even_count) # 3

# Edge Cases
arr2 = [0, 0, 0, 0]
odd_count, even_count = count_odd_even(arr2)
print("\nArray:", arr2)
print("Odd Count:", odd_count)   # 0
print("Even Count:", even_count) # 4

arr3 = [1]
odd_count, even_count = count_odd_even(arr3)
print("\nArray:", arr3)
print("Odd Count:", odd_count)   # 1
print("Even Count:", even_count) # 0

# Negative Case
arr4 = []
odd_count, even_count = count_odd_even(arr4)
print("\nArray:", arr4)
print("Odd Count:", odd_count)   # 0
print("Even Count:", even_count) # 0
