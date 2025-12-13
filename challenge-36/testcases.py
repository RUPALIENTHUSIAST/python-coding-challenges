# testcases.py
from solution import print_incremental_number_pattern

print("Running Test Cases for Incremental Number Pattern...\n")

# Positive Cases
print("Positive Case 1: N = 3")
print_incremental_number_pattern(3)
print()

print("Positive Case 2: N = 1")
print_incremental_number_pattern(1)
print()

print("Positive Case 3: N = 5")
print_incremental_number_pattern(5)
print()

# Edge Cases
print("Edge Case 1: N = 0 (should raise error)")
try:
    print_incremental_number_pattern(0)
except ValueError as e:
    print("Caught Error:", e)
print()

print("Edge Case 2: N = -5 (should raise error)")
try:
    print_incremental_number_pattern(-5)
except ValueError as e:
    print("Caught Error:", e)
print()

print("Edge Case 3: N = 1001 (should raise error for large input)")
try:
    print_incremental_number_pattern(1001)
except ValueError as e:
    print("Caught Error:", e)
print()

# Invalid Type Case
print("Invalid Type Case: N = 'abc' (should raise error)")
try:
    print_incremental_number_pattern("abc")
except TypeError as e:
    print("Caught Error:", e)
print()
