from solution import fibonacci_series

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print("N = 1 →", fibonacci_series(1))   # [1]
print("N = 2 →", fibonacci_series(2))   # [1, 1]
print("N = 5 →", fibonacci_series(5))   # [1, 1, 2, 3, 5]
print("N = 8 →", fibonacci_series(8))   # [1, 1, 2, 3, 5, 8, 13, 21]

# Edge Case
print("\nEdge Case:")
try:
    fibonacci_series(0)
except ValueError as e:
    print("N = 0 → Exception:", e)

# Negative Case
print("\nNegative Case:")
try:
    fibonacci_series(-5)
except ValueError as e:
    print("N = -5 → Exception:", e)
