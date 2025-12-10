from solution import calculate_simple_interest
print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print(f"Input: 1000, 5, 2  → {calculate_simple_interest(1000, 5, 2)}")  # 100 expected
print(f"Input: 5000, 7, 3  → {calculate_simple_interest(5000, 7, 3)}")  # 1050 expected

# Negative Cases (should raise error)
print("\nNegative Cases:")
try:
    calculate_simple_interest(-1000, 5, 2)
except ValueError as e:
    print(f"Input: -1000, 5, 2  → Exception: {e}")

try:
    calculate_simple_interest(1000, -5, 2)
except ValueError as e:
    print(f"Input: 1000, -5, 2  → Exception: {e}")

try:
    calculate_simple_interest(1000, 5, -2)
except ValueError as e:
    print(f"Input: 1000, 5, -2  → Exception: {e}")

# Edge Cases
print("\nEdge Cases:")
print(f"Input: 0, 5, 2  → {calculate_simple_interest(0, 5, 2)}")      # 0
print(f"Input: 1000, 0, 2 → {calculate_simple_interest(1000, 0, 2)}")  # 0
print(f"Input: 1000, 5, 0 → {calculate_simple_interest(1000, 5, 0)}")  # 0
