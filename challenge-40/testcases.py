from solution import print_fibonacci_pattern

print("Test Case 1: N = 1")
print_fibonacci_pattern(1)

print("\nTest Case 2: N = 4")
print_fibonacci_pattern(4)

print("\nTest Case 3: N = 6")
print_fibonacci_pattern(6)

print("\nTest Case 4: Invalid N")
try:
    print_fibonacci_pattern(0)
except Exception as e:
    print("Caught Error:", e)
