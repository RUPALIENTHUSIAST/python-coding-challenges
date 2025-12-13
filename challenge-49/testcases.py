# testcases.py

from solution import find_minimum

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print("Array: [5, 3, 9, 1, 7] → Minimum:", find_minimum([5, 3, 9, 1, 7]))  # 1
print("Array: [10, 20, 30] → Minimum:", find_minimum([10, 20, 30]))        # 10

# Edge Cases
print("\nEdge Cases:")
print("Array: [0, 0, 0] → Minimum:", find_minimum([0, 0, 0]))              # 0
print("Array: [-5, -10, 0] → Minimum:", find_minimum([-5, -10, 0]))         # -10
print("Array: [42] → Minimum:", find_minimum([42]))                         # 42

# Negative Case
print("\nNegative Case:")
try:
    find_minimum([])
except ValueError as e:
    print("Empty Array → Exception:", e)
