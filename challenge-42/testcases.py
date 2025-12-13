# testcases.py

from solution import print_factorial_pattern

print("Test Case 1: N = 1")
print_factorial_pattern(1)

print("\nTest Case 2: N = 3")
print_factorial_pattern(3)

print("\nTest Case 3: N = 5")
print_factorial_pattern(5)

print("\nEdge Case: N = 0")
try:
    print_factorial_pattern(0)
except Exception as e:
    print("Caught Error:", e)

print("\nEdge Case: Negative N")
try:
    print_factorial_pattern(-3)
except Exception as e:
    print("Caught Error:", e)
