from solution import generate_series

print("Running Test Cases...\n")

# Positive Case
print("Positive Case:")
print(generate_series(8))  
# Expected: [1, 5, 9, 13, 21, 25, 29, 37]

# Edge Case
print("\nEdge Case:")
print(generate_series(1))  # [1]

# Negative Case
print("\nNegative Case:")
try:
    generate_series(0)
except ValueError as e:
    print("Error:", e)
