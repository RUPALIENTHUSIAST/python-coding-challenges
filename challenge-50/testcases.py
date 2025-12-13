# testcases.py

from solution import find_maximum

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print("Array: [5, 3, 9, 1, 7] → Maximum:", find_maximum([5, 3, 9, 1, 7]))  # 9
print("Array: [10, 20, 30] → Maximum:", find_maximum([10, 20, 30]))        # 30

# Edge Cases
print("\nEdge Cases:")
print("Array: [0, 0, 0] → Maximum:", find_maximum([0, 0, 0]))              # 0
print("Array: [-5, -10, 0] → Maximum:", find_maximum([-5, -10, 0]))         # 0
print("Array: [42] → Maximum:", find_maximum([42]))                         # 42

# Negative Case
print("\nNegative Case:")
try:
    find_maximum([])
except ValueError as e:
    print("Empty Array → Exception:", e)
