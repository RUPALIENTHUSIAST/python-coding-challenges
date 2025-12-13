from solution import print_alternating_square_pattern

print("Running Test Cases...\n")

# Test Case 1: Normal case
print("Test Case 1: N = 4")
print_alternating_square_pattern(4)

# Test Case 2: Minimum valid input
print("\nTest Case 2: N = 1")
print_alternating_square_pattern(1)

# Test Case 3: Invalid input (zero)
print("\nTest Case 3: N = 0")
try:
    print_alternating_square_pattern(0)
except Exception as e:
    print("Caught Error:", e)

# Test Case 4: Invalid input (negative)
print("\nTest Case 4: N = -3")
try:
    print_alternating_square_pattern(-3)
except Exception as e:
    print("Caught Error:", e)

# Test Case 5: Invalid input (non-integer)
print("\nTest Case 5: N = 'five'")
try:
    print_alternating_square_pattern("five")
except Exception as e:
    print("Caught Error:", e)
