from solution import generate_series

print("Running Test Cases...\n")

# Test Case 1
print("Test Case 1 (N = 6):")
print(generate_series(6))
# Expected: [1, -5, 9, -13, 17, -21]

# Test Case 2
print("\nTest Case 2 (N = 1):")
print(generate_series(1))
# Expected: [1]

# Test Case 3
print("\nTest Case 3 (N = 10):")
print(generate_series(10))

# Negative Case
print("\nNegative Case:")
try:
    generate_series(-3)
except Exception as e:
    print("Caught Error:", e)
