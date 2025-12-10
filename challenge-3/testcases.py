from solution import calculate_discount

print("Running Test Cases...\n")

# Positive Cases
print("Positive Cases:")
print(f"Input: 1000, 10 → {calculate_discount(1000, 10)}")   # 900
print(f"Input: 500, 25 → {calculate_discount(500, 25)}")     # 375

# Negative Cases (should raise error)
print("\nNegative Cases:")
try:
    calculate_discount(-1000, 10)
except ValueError as e:
    print(f"Input: -1000, 10 → Exception: {e}")

try:
    calculate_discount(1000, -10)
except ValueError as e:
    print(f"Input: 1000, -10 → Exception: {e}")

try:
    calculate_discount(1000, -150)
except ValueError as e:
    print(f"Input: 1000, -150 → Exception: {e}")

# Edge Cases
print("\nEdge Cases:")
print(f"Input: 1e9, 50 → {calculate_discount(1e9, 50)}")         # 0
print(f"Input: 1e12, 0.5 → {calculate_discount(1e12, 0.5)}")     # 1000
print(f"Input: 123456789,12.34 → {calculate_discount(123456789, 12.34)}") # 0
